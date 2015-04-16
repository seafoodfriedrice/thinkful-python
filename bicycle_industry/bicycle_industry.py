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
        self.bicycle_inventory = {}
        self.store_balance = 1000
        # Q: Better to track profit here or in main()?
        self.profit = 0

    def add_bicycle(self, bicycle):
        """
        if bicycle.model not in self.bicycle_inventory:
            self.bicycle_inventor[bicycle.model] = []
        self.bicycle_inventory[bicycle.model].append(bicycle)
        """
        # Using dictionary setdefault to do the same as above
        """
        self.bicycle_inventory.setdefault(bicycle.model, [])
        self.bicycle_inventory[bicycle.model].append(bicycle)
        """
        # Even shorter
        self.bicycle_inventory.setdefault(bicycle.model, []).append(bicycle)
        self.store_balance -= bicycle.production_cost

    def sell(self, bicycle_model, customer):
        if bicycle_model in self.bicycle_inventory:
            if len(self.bicycle_inventory[bicycle_model]) > 0:
                # Q: Next two lines seem unnecessarily long, is there
                #    a cleaner way?
                bicycle_price = self.bicycle_inventory[bicycle_model][0].price
                bicycle_production_cost = self.bicycle_inventory[bicycle_model][0].production_cost
                if customer.budget >= bicycle_price:
                    self.profit += bicycle_price - bicycle_production_cost
                    self.bicycle_inventory[bicycle_model].pop()
                    self.store_balance += bicycle_price
                    customer.budget = customer.budget - bicycle_price
                    print "\nSold {} bicycle to {} for ${}.".format(
                        bicycle_model, customer.name, bicycle_price)
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

    """def display_profit(self):"""


class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bicycles_owned = []
    """def purchase_bicycle(self, bicycle_shop, bicycle_model):"""

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
    # Q: More elegant way to pass individual customers to sell() method?
    my_shop.sell("Green", customers[0])
    my_shop.sell("Red", customers[1])
    my_shop.sell("Black", customers[2])
    print
    my_shop.show_inventory()
    print "\n{}'s profit is now ${}.".format(my_shop.shop_name, my_shop.profit)

if __name__ == '__main__':
    main()
