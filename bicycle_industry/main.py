from bicycles_challenge import *

def main():
    monsanto = BicycleManufacturer('Monsanto', ['Zeus', 'Athena', 'Ares'])
    print "{} carries the following bicycle models: {}".format(
            monsanto.manufacturer_name,monsanto.models)
    comcast = BicycleManufacturer('Comcast', ['Poseidon', 'Hermes', 'Hera'])
    print "{} carries the following bicycle models: {}".format(
            comcast.manufacturer_name,comcast.models)

    print
    my_shop = BicycleShop("Pedal Files")
    
    for m in ['Zeus', 'Athena', 'Ares', 'Ares']:
        print "Purchasing {} from {}.".format(m, monsanto.manufacturer_name)
        my_shop.add_bicycle(monsanto.order(m))
    for c in ['Poseidon', 'Hermes', 'Hermes', 'Hera']:
        print "Purchasing {} from {}.".format(c, comcast.manufacturer_name)
        my_shop.add_bicycle(comcast.order(c))

    print "\n{}'s store balance is ${}.".format(my_shop.shop_name, my_shop.store_balance)
    print "{}'s store profit is ${}.\n".format(my_shop.shop_name, my_shop.profit)
    my_shop.show_inventory()
    print

    customers = [
        Customer("Cyclops", 200),
        Customer("Gambit", 500),
        Customer("Wolverine", 1000)
    ]

    for customer in customers:
        print "{} has a budget of ${}.".format(customer.name,customer.budget)
        print "{} can afford the following bicycles:".format(customer.name, my_shop.shop_name)
        for bicycle in my_shop.bicycle_inventory.values():
            bicycle = bicycle[0]
            if customer.budget >= my_shop.sell_price(bicycle.model):
                print "* {} ${}".format(bicycle.model, my_shop.sell_price(bicycle.model))
        print

    bicycles = ['Hera', 'Athena', 'Zeus']
    for bicycle, customer in zip(bicycles, customers):
        my_shop.sell(bicycle, customer)

    print
    my_shop.show_inventory()
    print "\n{}'s profit is now ${}.".format(my_shop.shop_name, my_shop.profit)

if __name__ == '__main__':
    main()
