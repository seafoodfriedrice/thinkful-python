import psycopg2
import logging
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
connect_args = {
    'host': 'localhost',
    'dbname': 'snippets',
    'user': 'postgres',
    'password': 'postgres'
}
connection = psycopg2.connect(**connect_args)
logging.debug("Database connection established.")

def put(name, snippet, hide):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    with connection, connection.cursor() as cursor:
        try:
            command = "insert into snippets values (%s, %s, %s)"
            cursor.execute(command, (name, snippet, hide))
        except psycopg2.IntegrityError as e:
            connection.rollback()
            if not hide:
                command = "update snippets set message=%s where keyword=%s"
                cursor.execute(command, (snippet, name))
            else:
                command = "update snippets set message=%s, hidden=%s where keyword=%s"
                cursor.execute(command, (snippet, hide, name))
    logging.debug("Snippet stored successfully.")
    return name, snippet, hide

def get(name):
    """Retrieve the snippet with a given keyword."""
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where "
                       "keyword=%s", (name,))
        row = cursor.fetchone()
    if not row:
        logging.debug("Failed to retrieve snippet.")
    else:
        logging.debug("Retrieved snippet successfully.")
        return row

def catalog():
    """Show available keywords to access snippets."""
    logging.info("Retrieving all keywords.")
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword from snippets order by keyword")
        return cursor.fetchall()

def search(string):
    """Search for string in snippets and return keyword and message."""
    logging.info("Searching for {} in database.".format(string))
    with connection, connection.cursor() as cursor:
        # Prepend and append % to string to use 'like' SQL statement
        string = "%{}%".format(string)
        cursor.execute("select * from snippets where message like %s",
                        (string,))
        return cursor.fetchall()

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(
                      description="Store and retrieve snippets of text")
    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("--hide",
                            help="Store snippet as hidden",
                            action='store_true')
    # Q: How to handle additional optional argument?
    #    This needs to be updated on Line 111 and elsewhere, etc.
    #put_parser.add_argument("--show",
    #                        help="Snippet will be be shown by default",
    #                        action='store_false')

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snipper")
    get_parser.add_argument("name", help="The name of the snippet")

    # Subparser for catalog()
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog",
                                           help="Display available keywords")

    # Subparser for search()
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search",
                                          help="Search for specific string")
    search_parser.add_argument("string", help="String to search in messages")

    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet, hide = put(**arguments)
        print ("Store {!r} as {!r} {}.".format(snippet, name, hide))
    elif command == "get":
        snippet = get(**arguments)
        print ("Retrieved snipper: {!r}".format(snippet))
    elif command == "catalog":
        keywords = catalog(**arguments)
        print ("Available snippet keywords: {!r}".format(keywords))
    elif command == "search":
        results = search(**arguments)
        print "Search found the following:\n"
        for result in results:
            print "{}: {}".format(result[0], result[1])

if __name__ == '__main__':
    main()
