import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(raw_input("Enter a number: "))
    
print "Fizz Buzz counting up to {0}".format(n)
for i in range(1, n+1):
    if (i % 3 == 0) and (i % 5 == 0):
        print "Fizz Buzz"
    elif (i % 3 == 0):
        print "Fizz"
    elif (i % 5 == 0):
        print "Buzz"
    else:
        print i