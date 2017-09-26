#Simple decorator working

def simple_decorator(f):
    #This function will be used in place of orignal definition
    def wrapper():
        print("Entering function wrapper in simple_decorator function")
        f()
        print("Exiting function wrapper in simple decorator")

    return wrapper

@simple_decorator
def hello1():
    print("I am the hello1 function")


#Decorators with arguments
def decorator_factory(enter_message, exit_message):
    #This decorator is to be returned
    def simple_decorator(f):
        def wrapper():
            print("Enter message: ", enter_message)
            f()
            print("Exit message: ", exit_message)
        return wrapper

    return simple_decorator

@decorator_factory('Start', 'End')
def hello2():
    print('I am the hello2 function')


if __name__ == '__main__':
    #print("Calling hello1 function now: ")
    #hello1()
    print("Calling the hello2 function")
    hello2()
