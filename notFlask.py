#!/usr/bin/python3

class NotFlask():
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError('Route "{}" has not been registered'.format(path))

app = NotFlask()

@app.route('/')
def hello():
    return 'Welcome to Flask internals'

print(app.serve('/'))


