def simple_decorator(f):
    #This function will be used in place of orignal definition
    def wrapper():
        print("Entering function wrapper in simple_decorator function")
        f()
        print("Exiting function wrapper in simple decorator")

    return wrapper

@simple_decorator
def hello():
    print("I am the hello function")

if __name__ == '__main__':
    print("Calling hello function now: ")
    hello()
