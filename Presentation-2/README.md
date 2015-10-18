# Flask

### What Is Flask

Flask is a popular web framework for Python enabling the development of reliable, scalable, and maintainable web applications. Flask was first released in 2010 and the latest version is 0.10.1.

Flask's developers refer to Flask as a microframework. "Micro" means that the core of Flask is simple yet extensible. Flask is modular and does not include anything that existing libraries already support such as a database abstraction layer or form validation. Developers are free to make their applications as small as possible, use libraries and frameworks they already understand, and install extensions when necessary that Flask promises to support.

"Micro" also means that Flask is easy to install and get running. Flask's Hello World App looks like this:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

What does this do?

1. First we imported the Flask class.
2. Then, we set a variable ```app``` to be a new instance of the Flask class.
3. We mapped the URL ```/``` to a function ```hello()``` meaning that when that URL is navigated to ```hello()``` will execute, in this case simply displaying the text "Hello World!"
4. Finally, ```run()``` will run the app on a local server.

Setting up Flask and running the Hello World app is easy as well:

```
$ pip install Flask
$ python hello.py
 * Running on http://localhost:5000/
```

Other popular Python web frameworks include Django, Web.py, Bottle, and MorePath that may be compared in this [roundup](http://www.konstruktor.ee/blog/python-web-framework-roundup/) and the same app built across multiple frameworks is included in this [repository](https://github.com/makaimc/compare-python-web-frameworks).

### Jinja2 Template Engine 

Flask can also be called a micro glue framework since it combines the [Jinja2 Template Engine](http://jinja.pocoo.org/2/) and the [Werkzeug](http://werkzeug.pocoo.org/documentation/) toolkit. Keeping in line with Flask's "micro" nature, while both are required to install Flask, developers may choose to use a templatting engine other than Jinja.

[Flask's specific integration with Jinja2 is documented here.](http://flask.pocoo.org/docs/0.10/templating/#jinja-setup)

### Werkzeug Templatting




### Tutorials I Followed in Learning the Basics

```
$ python helloFlask.py 
 * Running on http://127.0.0.1:5000/

$ python flaskr.py 
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader

$ python flaskr_tests.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.038s

OK

```