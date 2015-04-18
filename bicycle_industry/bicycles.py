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


class Wheel(object):
    def __init__(self, model, wheel_type, weight, production_cost):
        self.model = model
        self.wheel_type = wheel_type
        self.weight = weight
        self.production_cost = production_cost


class Frame(object):
    frame_types = ['aluminum', 'carbon', 'steel']
    def __init__(self, frame_type, weight, production_cost):
        self.frame_type = frame_type
        self.weight = self.frame_types[frame_type]
        self.production_cost = production_cost


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
