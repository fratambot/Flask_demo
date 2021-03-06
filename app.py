from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


#print(__name__)
app = Flask(__name__) # we run it as main, see below
app.config['SECRET_KEY'] = 'a-not-very-secret-key' # this should not be here but it should rather be an env variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # we use the simplest. If in production we want to pass to Postgre, sqlalchemy manages it and we don't need to change our model

db = SQLAlchemy(app)

# the routes are separated (best practice)
from routes import *


if __name__ == '__main__':
    app.run(debug=True) # always use degug in order to have useful info from Flask
    # notice that when you save the app is updated and restarted; don't need to ctrl+c and run it again
