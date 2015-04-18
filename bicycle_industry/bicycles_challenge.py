from collections import defaultdict

class Bicycle(object):
    def __init__(self, model):
        models = {
            'Zeus': { 'wheel': Wheel('cart'), 'frame': Frame('aluminum') },
            'Athena': { 'wheel': Wheel('ferris'), 'frame': Frame('aluminum') },
            'Ares': { 'wheel': Wheel('ferris'), 'frame': Frame('carbon') },
            'Poseidon': { 'wheel': Wheel('steering'), 'frame': Frame('carbon') },
            'Hermes': { 'wheel': Wheel('steering'), 'frame': Frame('steel') },
            'Hera': { 'wheel': Wheel('cart'), 'frame': Frame('steel') }
        }
        self.model = model
        self.wheel = models[model]['wheel']
        self.frame = models[model]['frame']
        self.margin_percent = 20
        self.total_production_cost = ((self.wheel.production_cost * 2) + 
                                      self.frame.production_cost)
        # Q: What is simplest way to ensure there are two decimal places?
        self.price = (self.total_production_cost + (self.total_production_cost *
                      (float(self.margin_percent) / 100)))


class Wheel(object):
    def __init__(self, model):
        wheels = {
            'cart': { 'weight': 10, 'production_cost': 20 },
            'ferris': { 'weight': 15, 'production_cost': 40 },
            'steering': { 'weight': 25, 'production_cost': 60 }
        }
        self.model = model
        self.weight = wheels[model]['weight']
        self.production_cost = wheels[model]['production_cost']


class Frame(object):
    def __init__(self, frame_type):
        frames = {
            'aluminum': { 'weight': 20, 'production_cost': 150 },
            'carbon': { 'weight': 30, 'production_cost': 100 },
            'steel': { 'weight': 40, 'production_cost': 75 }
        }
        self.frame_type = frame_type
        self.weight = frames[frame_type]['weight']
        self.production_cost = frames[frame_type]['production_cost']


class BicycleShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.bicycle_inventory = defaultdict(list)
        self.store_balance = 1000
        self.profit = 0

    def add_bicycle(self, bicycle):
        self.bicycle_inventory[bicycle.model].append(bicycle)
        self.store_balance -= bicycle.total_production_cost

    def sell(self, bicycle_model, customer):
        if bicycle_model in self.bicycle_inventory:
            if self.bicycle_inventory[bicycle_model]:
                bicycle = self.bicycle_inventory[bicycle_model][0]
                if customer.budget >= bicycle.price:
                    self.profit += bicycle.price - bicycle.total_production_cost
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
