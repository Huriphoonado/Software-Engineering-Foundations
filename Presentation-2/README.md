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

Flask can also be described as a micro glue framework since it combines the [Jinja2 Template Engine](http://jinja.pocoo.org/2/) and the [Werkzeug](http://werkzeug.pocoo.org/documentation/) toolkit. Keeping in line with Flask's "micro" nature, while both are required to install Flask, developers may choose to use a templatting engine other than Jinja.

A template is simply a text file containing variables and expressions that are replaced with values once the template is rendered. The following is the template used in the Flaskr mini blog tutorial (included in the Flask_Tutorials directory).

```
<!doctype html>
<title>Flaskr</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
  <h1>Flaskr</h1>
  <div class="metanav">
  {% if not session.logged_in %}
    <a href="{{ url_for('login') }}">log in</a>
  {% else %}
    <a href="{{ url_for('logout') }}">log out</a>
  {% endif %}
  </div>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block body %}{% endblock %}
  {# Also, a comment! #}
</div>
```

Jinja2 contains a few kinds of delimiters, some of which are used above.

* ```{% ... %}``` for [statements and control structures](http://jinja.pocoo.org/docs/dev/templates/#list-of-control-structures) such as for/if/else.
  * In the example above, statements are used to check whether a user is logged in or not as well to iterate through all messages that will fill out the body of the app.
* ```{{ ... }}``` for [expressions to print to the template output](http://jinja.pocoo.org/docs/dev/templates/#expressions)
  * In the example above, expressions are used to display either a login or logout button and any messages or entries stored in the database
* ```{# ... #}``` for [comments not included in the template output](http://jinja.pocoo.org/docs/dev/templates/#comments)
* ```#  ... ##``` for [line statements](http://jinja.pocoo.org/docs/dev/templates/#line-statements)

As is described on [Flask's Template Inheritance](http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/#template-inheritance) page, one of the most powerful aspects of Jinja2 is its capability for template inheritance. Template Inheritance enables a basic template frame containing all common elements of a website to be filled in by child templates containing other content, eg. comments on a blog post or website tools only admins can access. In the Flaskr example, login.html and show_entries.html are both child templates of layout.html - login.html is shown below.

```
{% extends "layout.html" %}
{% block body %}
  <h2>Login</h2>
  {% if error %}<p class="error"><strong>Error:</strong> {{ error }}{% endif %}
  <form action="{{ url_for('login') }}" method="post">
    <dl>
      <dt>Username:
      <dd><input type="text" name="username">
      <dt>Password:
      <dd><input type="password" name="password">
      <dd><input type="submit" value="Login">
    </dl>
  </form>
{% endblock %}
```

Child templates must begin with the ```{% extends %}``` tag indicating its parent and then contain its content within a ```{% block %}``` tag in which case it will overwrite the same ```{% block %}``` tag in the parent document.

[Jinja's template designer documentation may be found here.](http://jinja.pocoo.org/docs/dev/templates/#list-of-control-structures)

[Flask's specific integration with Jinja2 is documented here.](http://flask.pocoo.org/docs/0.10/templating/#jinja-setup)

### Werkzeug

Werkzeug is the base of Flask and is an advanced WSGI utility module enabling web applications built with Python to communicate with a webserver. It is essentially middleware that can be used to build frameworks (like Flask) or web applications. [Flask in particular uses Werkzeug for its routing system](http://werkzeug.pocoo.org/docs/0.10/routing/) which is designed to order routes by complexity meaning they can be declared in an arbitrary order and to ensure that URLs are unique.

Werkzeug's Hello World application looks like this:

```
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('Hello World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
```

* The Request object wraps the WSGI Environment (which contains all the information the user request transmits to the application) and provides read-only access to the data.
* The Response object is a WSGI application that may be used to send data back to the server.

### Installing and Getting Started With Flask

The makers of Flask and Werkzeug recommend first and foremost that all developers use [virtualenv](https://virtualenv.pypa.io/en/latest/), a tool to create isolated Python environments.

```
$ sudo pip install virtualenv
...
$ virtualenv --version
13.1.2
```

Virtualenv allows you to work with a specific version of Python and specific libraries within an isolated project preventing multiple projects with different dependencies from breaking eachother. A virtual environment can be created within your project directory.

```
$ mkdir newproj
$ cd newproj/
$ virtualenv venv --python=python2.7
Running virtualenv with interpreter /opt/local/bin/python2.7
New python executable in venv/bin/python
Installing setuptools, pip, wheel...done.
```

Whenever you want to work on your project you may activate the virtual environment via the following command:

```
Willie-Paynes-MacBook-Pro:newproj williepayne$ . venv/bin/activate
(venv)Willie-Paynes-MacBook-Pro:newproj williepayne$
(venv)Willie-Paynes-MacBook-Pro:newproj williepayne$ deactivate
Willie-Paynes-MacBook-Pro:newproj williepayne$ 
```

Finally, you may install Flask:

```
$ pip install Flask
...

```

### Flask Routes

Like all modern web applications Flask enables the developer to select clear URLs and map specific functions to them. The ```route()``` decorator binds a function to a URL. 

```
@app.route('/')
def index():
    pass

@app.route('/hello')
def hello():
    return 'Hello World' # display some text (eg at http://localhost:5000/hello)

@app.route('/about-me')
def footer():
	return render_template(about-me.html) # render a template
```

URLs can contain variables marked as ```<variable>``` as well. By default, variables accept strings, but other datatypes (int, float, path) called converters may be specified: ```<converter:variable>```

```
@app.route('/user/<username>') # Include the username in the url
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>') # grab the integer post id
def show_post(post_id):
    return 'Post %d' % post_id
```

Finally, Flask has specific rules about the use of trailing slashes to make sure that URLs are all kept unique.

1. If a URL ends with a slash (eg ```@app.route('/hello/')```) and is navigated to without a slash, the user is automatically redirected to the same page with a trailing slash attached.
2. However, if the URL is defined without a trailing slash and the user navigates to the URL with a trailing slash, he/she will reach a 404 error.

Flasks' documentation on URLS may be found [here](http://flask.pocoo.org/docs/0.10/api/#url-route-registrations) and information on Flask's URL building feature may be found [here](http://flask.pocoo.org/docs/0.10/quickstart/#url-building).

### HTTP Methods

### Flask Project Structure

A smaller application may look like this:

```
/yourapplication
    /yourapplication.py
    /static
        /style.css
    /templates
        layout.html
        index.html
        login.html
        ...
```

Flask recommends that larger applications are contained within an extra directory and that the main python document is named to __init__.py. [Larger applications may look more like this](http://flask.pocoo.org/docs/0.10/patterns/packages/):

```
/yourapplication
    /runserver.py
    /yourapplication
        /__init__.py
        /views.py
        /static
            /style.css
        /templates
            layout.html
            index.html
            login.html
            ...
```

This arrangement allows the application to be broken down into multiple modules. The file runserver.py is responsible for actually running the application:

```
from yourapplication import app
app.run(debug=True)
```

The file __init__.py is responsible for creating the Flask object:

```
from flask import Flask
app = Flask(__name__)

import yourapplication.views
```

The file views.py is responsible is responsible for all of the view functions:

```
from yourapplication import app

@app.route('/')
def index():
    return 'Hello World!'
```

### Tutorials I Followed in Learning the Basics

```
$ python helloFlask.py 
 * Running on http://127.0.0.1:5000/

$ python flaskr.py 
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader

$ python flaskr_tests.py 
----------------------------------------------------------------------
Ran 3 tests in 0.038s

OK
```

If the previous example does not work, there may have been a problem creating the required tables in the database. In a python shell within the willie_blog directory, type the following and it should work:

```
>>> from flaskr import init_db
>>> init_db()
```