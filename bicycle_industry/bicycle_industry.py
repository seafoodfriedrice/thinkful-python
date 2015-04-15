class Bicycle(object):
    def __init__(self, model, weight, production_cost):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost

class BicycleShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.bicycle_inventory = []
        self.store_balance = 1000

    def add_bicycle(self, bicycle):
        self.bicycle_inventory.append(bicycle)
        self.store_balance = self.store_balance - bicycle.production_cost
        
    def sell(self, bicycle, margin_percent):
        for bicycle in self.bicycle_inventory:
            if isinstance(bicycle, Bicycle):
                sell_price = bicycle.production_cost + (bicycle.production_cost
                             * (float(margin_percent) / 100.0))
                self.bicycle_inventory.remove(bicycle)
                self.store_balance = self.store_balance + sell_price

    def show_inventory(self):
        for bicycle in self.bicycle_inventory:
            print "{} bicycle inventory:".format(self.shop_name)
            # How to correctly calculate margin cost and display
            print "* {}".format(bicycle.model, bicycle.weight, bicycle.production_cost)

    def display_profit(self):

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.funds = funds
        self.bicycles_owned = []

    def purchase_bicycle(self, bicycle_shop, bicycle_model):
        

my_shop = BicycleShop("Pedal Files")
my_shop.add_bicycle(Bicycle("Green", 50, 150))
my_shop.add_bicycle(Bicycle("Blue", 75, 200))
my_shop.add_bicycle(Bicycle("Red", 100, 250))
my_shop.add_bicycle(Bicycle("Silver", 125, 300))
my_shop.add_inventory(Bicycle("Gold", 125, 500))
my_shop.add_inventory(Bicycle("Black", 100, 750))

customer_one = Customer("Cyclops", 200)
customer_two = Customer("Gambit", 500)
customer_three = Customer("Wolverine", 1000)
