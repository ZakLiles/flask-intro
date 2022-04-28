"""Greeting Flask app."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['awful', 'unpleasant', 'eww', 'terrible', 'horrible', 'positively dreadful', 'horrendous']

@app.route('/')
def start_here():
    """Home page."""

    return render_template('home.html')


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return render_template('hello.html', awesomeness = AWESOMENESS, insults = INSULTS)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def dis_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
