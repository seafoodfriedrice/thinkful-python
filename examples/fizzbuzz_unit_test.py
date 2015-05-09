def fizzbuzz(n):
    ret = ""
    if not (n % 3):
        ret += "fizz"
    if not (n % 5):
        ret += "buzz"
    return ret or str(n)

def fizzbuzz_test(f):
    if f(3) == "fizz" and f(5) == "buzz" and f(15) == "fizzbuzz":
        print("Success!")
    else:
        print("Nope. Try again.")

fizzbuzz_test(fizzbuzz)
