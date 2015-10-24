# Flask

### What Is Flask

Flask is a popular web framework for Python enabling the development of reliable, scalable, and maintainable web applications. Flask was first released in 2010 and the latest version is 0.10.1.

Flask's developers refer to Flask as a microframework. "Micro" means that the core of Flask is simple yet extensible. Flask is modular and does not include anything that existing libraries already support such as a database abstraction layer or form validation. Developers are free to make their applications as small as possible, use libraries and frameworks they already understand, and install extensions when necessary that Flask promises to support.

"Micro" also means that Flask is easy to install and get running. Flask's Hello World app looks like this:

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

### The Flask Object

The first thing you will want to do in your main module or in the __init.py__ file of your package (described later) is to create an instance of the Flask object. 

```
from flask import Flask
app = Flask(__name__)
```

The flask object implements a WSGI application and is passed the name of the module or package of the application. It acts as a central registry for the view functions, the URL rules, template configuration and much more. In an application with only a single module module, 

[The Flask Object can take in the parameters described here in the Flask API.](http://flask.pocoo.org/docs/0.10/api/)

### URL Routing

Like all modern web applications Flask enables the developer to pick exact URLs and map specific functions to them. The ```route()``` decorator binds a function to a URL. 

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

Flask allows you to include an [HTTP methods](http://www.w3schools.com/tags/ref_httpmethods.asp) argument in the ```route()``` decorator. (The argument defaults to ```'GET'```.) In the Flaskr demo app, 'GET' is used when simply displaying blog posts, ```@app.route('/')```, 'POST' is used when submitting blog posts, ```@app.route('/add, methods=['POST'])```, and both are used when inviting the user to log in and display his/her status, ```@app.route('/login', methods=['GET', 'POST'])```. Flask supports a few HTTP methods:

* GET - Retrieve information from the server. GET requests may be cached and remain in the browser history.
* POST - Submit information to be processed and stored. The server must ensure that the data is only stored once. POST requests may not be cached or remain in the browser history.
* HEAD - Only return HTTP headers and not the document body.
* PUT - Similar to POST, but the server may store the submitted data multiple times potentially making the request more reliable.
* DELETE - Remove the specified resource.

### Flask View Functions

Much of your time spent developing apps with Flasks will be spent building view functions which provide application logic, render template files, and interface with the application's database. We will look in depth at the view functions used in the Flaskr tutorial app.

#### ```show_entries()``` displays a list of blog posts:

```
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
```

* Map the URL ```/``` to ```show_entries()```.
* Query the database for the title and text of all entries, and convert the results into a dict ```entries```.
* Render the template show_entries.html passing the ```entries``` dict to the template.

#### ```add_entry()``` allows the user to add new blog posts:

```
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
```

* Map the URL ```/add``` to ```add_entry()``` and indicate that information can be submitted.
* If the user trys to add a post, but is not logged in, prevent submission and display a 401 error. (This will occur if the user types in the ```/add``` url.)
* Otherwise, add the entry to the database (being careful to use question marks which will prevent SQL injection) and commit the submission.
* Once the submission has successfully completed, [display a message with ```flash()```](http://flask.pocoo.org/docs/0.10/api/#flask.flash) and redirect the user back to the url used for the show entries function.

#### ```login()``` allows the user to login to the application:

```
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
```

* Map the URL ```/login``` to ```login()``` and indicate that information can be submitted and retrieved.
* If the user trys to submit information, check that the username and password are correct ('admin' and 'default' respectively).
* If either is incorrect, reload the login template passing in an error message.
* Otherwise, set the user's login status to True, display a message, and redirect the user to the url mapped to the ```show_entries()``` function. ([The ```session``` object](http://flask.pocoo.org/docs/0.10/api/#sessions) is imported from Flask that works as a dict, but keeps track of modifications.)

#### ```logout()``` allows the user to log out of the application:

```
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
```

* Map the URL ```/logout``` to ```logout()```.
* The ```pop()``` method of the ```session``` dict will delete the key from the session if it exists or do nothing if it doesn't effectively logging the user out.
* Redirect the user to the url mapped to the ```show_entries()``` function.

### Using A Database With Flask

As was previously mentioned, Flask does not enforce the use of any specific database, but provides documentation on using [SQLite 3](http://flask.pocoo.org/docs/0.10/patterns/sqlite3/) and [SQLAlchemy](http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/). We will cover SQLite 3 briefly. From the documentation:

```
import sqlite3
from flask import g

DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
```

* Import SQLite and the Flask g object which stores the current database connection. (THe SQLite library ships with all distributions of Python after Python 2.5.)
* The ```get_db()``` function will return the current database and ```close_connection(exception)``` will automatically terminate the database connection.

Flask recommends that developers open/close the connection before and after every request. Flask provides three helpful decorators.

1. Functions marked with ```before_request()``` are called before a request and are passed no arguments.
2. Functions marked with ```after_request()``` are called after a request and passed the response that will be sent to the client. However, these may not be executed if an exception is raised.
3. Functions marked with ```teardown_request()``` may not modify the request and are passed all exception values.

[Information on adding to, removing from, and querying a SQLite database may be found on Python's official documentation.](https://docs.python.org/2/library/sqlite3.html) For example, querying a books database may look like this:

```
connection = sqlite3.connect('books.db')

with connection:    
    
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM Books")

    rows = cursor.fetchall()

    for row in rows:
        print row
```

[Flask recommends providing a querying function that combines getting the cursor, executing, and fetching the results:](http://flask.pocoo.org/docs/0.10/patterns/sqlite3/#easy-querying)

```
def query_db(query, args=(), one=False):
    cursor = get_db().execute(query, args)
    retrieve = cursor.fetchall()
    cursor.close()
    return (retrieve[0] if retrieve else None) if one else retrieve

for user in query_db('select * from users'):
    print user['username'], 'has the id', user['user_id']

```

As is done in the Flaskr app, a function should be used to create the database based on an included schema. (In the case of the tutorial schema.sql is a single table containing auto-incrementing ids, titles, and descriptions for blog posts).

```
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()
```

The above code may be run to initialize the database using the following commands from within a python shell:

```
>>> from flaskr.py import init_db
>>> init_db()
```

### Testing Flask Apps



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

The file views.py is responsible for all of the view functions:

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

### Further Reading

