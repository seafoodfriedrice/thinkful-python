import functools

def twist(twister):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print twister
            function(*args, **kwargs)
        return wrapper
    return decorator

@twist("She sells sea shells on the sea shore")
def spoon():
    print "A well-boiled icicle"

spoon()
