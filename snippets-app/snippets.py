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

def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    with connection, connection.cursor() as cursor:
        try:
            command = "insert into snippets values (%s, %s)"
            cursor.execute(command, (name, snippet))
        except psycopg2.IntegrityError as e:
            command = "update snippets set message=%s where keyword=%s"
            cursor.execute(command, (snippet, name))
    logging.debug("Snippet stored successfully.")
    return name, snippet

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

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snipper")
    get_parser.add_argument("name", help="The name of the snippet")

    # Subparser for catalog()
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog",
                                           help="Display available keywords")

    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snipper = put(**arguments)
        print ("Store {!r} as {!r}".format(snipper, name))
    elif command == "get":
        snipper = get(**arguments)
        print ("Retrieved snipper: {!r}".format(snipper))
    elif command == "catalog":
        keywords = catalog(**arguments)
        print ("Available snippet keywords: {!r}".format(keywords))

if __name__ == '__main__':
    main()
