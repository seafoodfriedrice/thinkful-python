from bicycles import *

def main():
    my_shop = BicycleShop("Pedal Files")
    my_shop.add_bicycle(Bicycle(model="Green", weight=50, production_cost=150))
    my_shop.add_bicycle(Bicycle(model="Green", weight=50, production_cost=150))
    my_shop.add_bicycle(Bicycle(model="Green", weight=50, production_cost=150))
    my_shop.add_bicycle(Bicycle(model="Blue", weight=75, production_cost=200))
    my_shop.add_bicycle(Bicycle(model="Blue", weight=75, production_cost=200))
    my_shop.add_bicycle(Bicycle(model="Red", weight=100, production_cost=250))
    my_shop.add_bicycle(Bicycle(model="Silver", weight=125, production_cost=300))
    my_shop.add_bicycle(Bicycle(model="Gold", weight=125, production_cost=500))
    my_shop.add_bicycle(Bicycle(model="Black", weight=100, production_cost=750))

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
    f = Frame('carbon')
    w = Wheel('cart')
    print "Weight: {}, Production Cost: {}".format(f.weight, f.production_cost)
    print "Weight: {}, Production Cost: {}".format(w.weight, w.production_cost)
    #main()
