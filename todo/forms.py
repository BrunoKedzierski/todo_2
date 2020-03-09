from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class register_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=2, max=20)])
    confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')

class login_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])



