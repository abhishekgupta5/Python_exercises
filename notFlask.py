#!/usr/bin/python3

class NotFlask():

    # Dictionary to store routes
    def __init__(self):
        self.routes = {}

    #The decorator function
    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    #Function for serving the URL from dict 'routes'
    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError('Route "{}" has not been registered'.format(path))

#Object of the notFlask class
app = NotFlask()

#The decorator with URL as argument
@app.route('/')
def hello():
    return 'Welcome to Flask internals'

#Usage of the decorator
print(app.serve('/'))


