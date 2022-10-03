# PicoWebRouter

Web framework for the Pi Pico to emulate a flask like experience for serving webpages.

## How to Use

Instantiate web router with ip, port, and default html file to be used.

    app = PicoWebRouter("192.168.1.10",  80, ""/static/default.html")

Then add routes to the app using the `@app.route()` decorator. Also provide a route for it.

    @app.route("/test")
    def about_me(*args, **kwargs):
        return "MY HTML" 

Once you have associated all the routes you want you serve it using `app.serve()`

## What is provided to the routes as args/kwargs?

Currently the request is returned as on object. You can currently view all the different parts of a request including query strings and data. Check [here](/picowebrouter/objects/request.py) for object definition.

    @app.route("/test")
    def about_me(*args, **kwargs):
        request = kwargs.get("request")
        return "MY HTML" 