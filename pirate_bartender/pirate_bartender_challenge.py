import random

def ask_questions():
    questions = {
        "strong": "Do ye like yer drinks strong? ",
        "salty": "Do ye like it with a salty tang? ",
        "bitter": "Are ye a lubber who likes it bitter? ",
        "sweet": "Would ye like a bit of sweetness with yer poison? ",
        "fruity": "Are ye one for a fruity finish? "
    }
    preferences = {}
    for question in questions:
        response = raw_input(questions[question])
        if response == "yes" or response == "y":
            preferences[question] = True
        else:
            preferences[question] = False
    return preferences

def random_cocktail_name():
    adjectives = ["Fluffy", "Salty", "Bitter", "Fruity", "Strong", "Epic", "Crunchy", "Sandy"]
    nouns = ["Sea-Dog", "Puppy", "Island", "Spongebob", "Chinchilla", "Whale-Shark", "Tsunami"]
    return "{} {}".format(random.choice(adjectives), random.choice(nouns))

def construct_drink(preferences):
    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
    }
    drink = []
    for p in preferences:
        if preferences[p] == True:
            drink.append(random.choice(ingredients[p]))
    return drink

customers = {}

def main():
    customer_name = raw_input("What be yer name matey? ")
    if customer_name not in customers:
        customers[customer_name] = {}
        customers[customer_name]["drink_name"] = random_cocktail_name()
        customers[customer_name]["drink_ingredients"] = construct_drink(ask_questions())
    else:
        print "\nAy, welcome back {}. We got yer drink on file.".format(customer_name)
    print "\nYour drink, the {}, has the following ingredients:".format(customers[customer_name]["drink_name"])
    for ingredient in customers[customer_name]["drink_ingredients"]:
        print "* {}".format(ingredient)

if __name__ == '__main__':
    again = "y"
    while again != "n":
        main()
        again = raw_input("\nAnother round? ")
