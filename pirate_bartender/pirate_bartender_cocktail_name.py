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

def random_cocktail_name():
    adjectives = ["Fluffy", "Salty", "Bitter", "Fruity", "Strong", "Epic", "Crunchy", "Sandy"]
    nouns = ["Sea-Dog", "Puppy", "Island", "Spongebob", "Chinchilla", "Whale-Shark", "Tsunami"]
    return "{} {}".format(random.choice(adjectives), random.choice(nouns))

def main():
    drinks_preferred = construct_drink(ask_questions())
    print "\nYour drink, the {}, has the following ingredients:".format(random_cocktail_name())
    for ingredient in drinks_preferred:
        print "* {}".format(ingredient)

if __name__ == '__main__':
    main()
