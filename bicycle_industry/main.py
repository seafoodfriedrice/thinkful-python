from bicycles_challenge import *

def main():
    my_shop = BicycleShop("Pedal Files")
    bicycles = ['Zeus', 'Zeus', 'Athena', 'Ares', 'Poseidon', 'Hermes', 'Hera']
    for bicycle in bicycles:
        my_shop.add_bicycle(Bicycle(bicycle))
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

    print my_shop.bicycle_inventory

    bicycles = ['Zeus', 'Hera', 'Ares']
    for bicycle, customer in zip(bicycles, customers):
        my_shop.sell(bicycle, customer)

    print

    my_shop.show_inventory()

    print "\n{}'s profit is now ${}.".format(my_shop.shop_name, my_shop.profit)

if __name__ == '__main__':
    main()
