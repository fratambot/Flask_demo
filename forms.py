from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# It's pretty easy to create forms in Flask
from wtforms.validators import DataRequired # many validators, here we just want not leave it blank

class AddTaskForm(FlaskForm): # we create our class which inherits from FlaskForm
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete') # we pass the task and we can show the name but we don't need a field for that
