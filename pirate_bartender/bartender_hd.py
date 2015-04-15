from random import choice

customers = {}


def ask_questions():
    questions = {
        "strong": "Do ye like yer drinks strong? ",
        "salty": "Do ye like it with a salty tang? ",
        "bitter": "Are ye a lubber who likes it bitter? ",
        "sweet": "Would ye like a bit of sweetness with yer poison? ",
        "fruity": "Are ye one for a fruity finish? "
    }
    preferences = []
    for preference, question in questions.iteritems():
        response = raw_input(question)
        # A list of positive answers
        positives = ['yes', 'y', 'yeah', 'yay', 'ye']
        # Simply assign the result of the membership check
        if response.lower() in positives:
            preferences.append(preference)
    return preferences


def random_cocktail_name():
    adjectives = ["Fluffy", "Salty", "Bitter", "Fruity", "Strong", "Epic",
                  "Crunchy", "Sandy"]
    nouns = ["Sea-Dog", "Puppy", "Island", "Spongebob", "Chinchilla",
             "Whale-Shark", "Tsunami"]
    return "{} {}".format(choice(adjectives), choice(nouns))


def construct_drink(preferences):
    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic",
                   "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
    }

    return [choice(ingredients[p]) for p in preferences]


def main():
    customer_name = raw_input("What be yer name matey? ")
    if customer_name not in customers:
        customer = {}
        customer["drink_name"] = random_cocktail_name()
        customer["drink_ingredients"] = construct_drink(ask_questions())

        customers[customer_name] = customer
    else:
        customer = customers[customer_name]
        print "\nAy, welcome back {}. We got yer drink on file.".format(
            customer_name)

    print "\nYour drink, the {}, has the following ingredients:".format(
        customer["drink_name"])

    for ingredient in customer["drink_ingredients"]:
        print "* {}".format(ingredient)


if __name__ == '__main__':
    again = "y"
    while again.lower() not in ["no", "n", "nope", "nay"]:
        main()
        again = raw_input("\nAnother round? ")
