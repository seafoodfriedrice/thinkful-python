class Bicycle(object):
    def __init__(self, model, weight, production_cost):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost
        self.margin_percent = 20
        # Need to correctly display two decimal points on price
        self.price = self.production_cost + (self.production_cost *
                          (float(self.margin_percent) / 100))

class BicycleShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.bicycle_inventory = {}
        self.store_balance = 1000

    def add_bicycle(self, bicycle):
        if bicycle.model not in self.bicycle_inventory:
            self.bicycle_inventory[bicycle.model] = []
            self.bicycle_inventory[bicycle.model].append(bicycle)
        else:
            self.bicycle_inventory[bicycle.model].append(bicycle)
        self.store_balance = self.store_balance - bicycle.production_cost

    """
    def sell(self, bicycle, margin_percent, customer):
        for bicycle in self.bicycle_inventory:
            if isinstance(bicycle, Bicycle) and bicycle.name
                             * (float(margin_percent) / 100.0))
                self.bicycle_inventory.remove(bicycle)
                self.store_balance = self.store_balance + sell_price
    """

    def show_inventory(self):
        print "{} bicycle inventory:".format(self.shop_name)
        for bicycle_model, bicycle in self.bicycle_inventory.iteritems():
            print "> ({}) {} ${}".format(len(bicycle), bicycle_model, bicycle[0].price)

    """def display_profit(self):"""

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bicycles_owned = []

    def purchase_bicycle(self, bicycle_shop, bicycle_model):
        

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

print "{}'s store balance is ${}.\n".format(my_shop.shop_name, my_shop.store_balance)

customer_one = Customer("Cyclops", 200)
customer_two = Customer("Gambit", 500)
customer_three = Customer("Wolverine", 1000)

for customer in [customer_one, customer_two, customer_three]:
    print "{} has a budget of ${}.".format(customer.name,customer.budget)
    print "{} can afford the following bicycles:".format(customer.name, my_shop.shop_name)
    for bicycle_model, bicycle in my_shop.bicycle_inventory.iteritems():
        if customer.budget >= bicycle[0].price:
            print "* {}".format(bicycle[0].model)
    print

my_shop.show_inventory()
