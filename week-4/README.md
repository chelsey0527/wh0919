# Flask

In this week, we are implementing flask as our web back-end framework.

## 1. What is Flask?
Flask is a web framework, it’s a Python module that let us develop web applications easily. 
It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

## 2. Getting started
( to be continue)



<br>

# Flask Session
Allows us to store information specific to a user from one request to the next.
<br>

***Cookie-based session.*** You may understand it as a client-side based session implemeted on top of cookis.
<br>
Flask will take the values you put into the session object and serialize them into a cookie. 
<br>
User could look at the contents of your cookie instead of modify it, unless they know the signin secret key.
<br>

Cookies are small pieces of text sent to your browser by a website you visit. 
They help that website remember information about your visit, which can both make it easier to visit the site again and make the site more useful to you.
<br>
Cookies can cleard by ***clear browsing data*** function on your browser.

If you want to handle session of server-side instead, several [Flask extensions](https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/) support this.
<br>

## Getting Started
1. Import session from flask to your file
```python
from flask import session
```
2. Set the secret key to some random bytes. (Keep it secret👀) <br>
A secret key should be as random as possible.
```python
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
```
3. Quick example
```python
@app.route('/')
def index():
    # If the username was record (= user logged in), return to the target page.
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    # Else, remind the user to login for the page.
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # when user logged in, let flask session record the user's username.
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```



<br>

# Flask Dynamic Routing
