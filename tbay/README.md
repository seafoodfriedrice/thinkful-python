# Example output

```
(env) tbay $ dropdb tbay -U postgres
(env) tbay $ createdb tbay -U postgres
(env) tbay $ python tbay.py
```
```
(env) tbay $ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from tbay import *
>>> alice = User(username="alice", password="wonderland")
>>> bob = User(username="bob", password="builder")
>>> eve = User(username="eve", password="christmas")
>>> baseball = Item(name="baseball", description="standard issue baseball")
>>> alice.auctions.append(baseball)
>>> bid_bob = Bid(price=10.25, user=bob, item=baseball)
>>> bid_eve = Bid(price=11.00, user=eve, item=baseball)
>>> session.add_all([alice, bob, eve, baseball, bid_bob, bid_eve])
>>> session.commit()
>>> 
```

```
(env) tbay $ psql -U postgres tbay
psql (9.3.6)
Type "help" for help.

tbay=# select * from items;
 id |   name   |       description       |         start_time         | auction_id 
----+----------+-------------------------+----------------------------+------------
  1 | baseball | standard issue baseball | 2015-04-26 18:07:08.902858 |          1
(1 row)

tbay=# select * from users;
 id | username |  password  
----+----------+------------
  1 | alice    | wonderland
  2 | bob      | builder
  3 | eve      | christmas
(3 rows)

tbay=# select * from bids;
 id | price | item_id | user_id 
----+-------+---------+---------
  1 | 10.25 |       1 |       2
  2 |    11 |       1 |       3
(2 rows)
```
