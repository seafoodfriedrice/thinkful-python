from collections import defaultdict

class Bicycle(object):
    def __init__(self, model, weight, production_cost):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost
        self.margin_percent = 20
        # Q: What is simplest way to ensure there are two decimal places?
        self.price = self.production_cost + (self.production_cost *
                          (float(self.margin_percent) / 100))


class BicycleShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.bicycle_inventory = defaultdict(list)
        self.store_balance = 1000
        # Q: Better to track profit here or in main()?
        self.profit = 0

    def add_bicycle(self, bicycle):
        self.bicycle_inventory[bicycle.model].append(bicycle)
        self.store_balance -= bicycle.production_cost

    def sell(self, bicycle_model, customer):
        if bicycle_model in self.bicycle_inventory:
            if self.bicycle_inventory[bicycle_model]:
                bicycle = self.bicycle_inventory[bicycle_model][0]
                if customer.budget >= bicycle.price:
                    self.profit += bicycle.price - bicycle.production_cost
                    self.bicycle_inventory[bicycle_model].pop()
                    self.store_balance += bicycle.price
                    customer.budget = customer.budget - bicycle.price
                    print "\nSold {} bicycle to {} for ${}.".format(
                        bicycle.model, customer.name, bicycle.price)
                    print "{} has ${} left.".format(
                        customer.name, customer.budget)
                else:
                    print "\nSorry, {} cannot afford the {} bicycle on their budget.".format(
                        customer.name, bicycle_model)
            else:
                print "\nSorry, we don't have any {} bicycles left.".format(bicycle_model)
        else:
            print "\nSorry, we don't have any models called {}.".format(bicycle_model)

    def show_inventory(self):
        print "{} bicycle inventory:".format(self.shop_name)
        for bicycle_model, bicycle in self.bicycle_inventory.iteritems():
            # Does not display out of stack bicycles and their prices
            if self.bicycle_inventory[bicycle_model]:
                print "> ({}) {} ${}".format(len(bicycle), bicycle_model,
                                             bicycle[0].price)

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bicycles_owned = []


def main():
    my_shop = BicycleShop("Pedal Files")
    my_shop.add_bicycle(Bicycle("Green", 50, 150))
    my_shop.add_bicycle(Bicycle("Green", 50, 150))
    my_shop.add_bicycle(Bicycle("Green", 50, 150))
    my_shop.add_bicycle(Bicycle("Blue", 75, 200))
    my_shop.add_bicycle(Bicycle("Blue", 75, 200))
    my_shop.add_bicycle(Bicycle("Red", 100, 250))
    my_shop.add_bicycle(Bicycle("Silver", 125, 300))
    my_shop.add_bicycle(Bicycle("Gold", 125, 500))
    my_shop.add_bicycle(Bicycle("Black", 100, 750))

    print "{}'s store balance is ${}.".format(my_shop.shop_name, my_shop.store_balance)
    print "{}'s store profit is ${}.\n".format(my_shop.shop_name, my_shop.profit)

    customers = [
        Customer("Cyclops", 200),
        Customer("Gambit", 500),
        Customer("Wolverine", 1000)
    ]

    for customer in customers:
        print "{} has a budget of ${}.".format(customer.name,customer.budget)
        print "{} can afford the following bicycles:".format(customer.name, my_shop.shop_name)
        for bicycle_model, bicycle in my_shop.bicycle_inventory.iteritems():
            if customer.budget >= bicycle[0].price:
                print "* {}".format(bicycle[0].model)
        print

    my_shop.show_inventory()
    colors = ['Green', 'Red', 'Black']
    for color, customer in zip(colors, customers):
        my_shop.sell(color, customer)
    print
    my_shop.show_inventory()
    print "\n{}'s profit is now ${}.".format(my_shop.shop_name, my_shop.profit)

if __name__ == '__main__':
    main()
