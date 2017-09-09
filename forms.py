from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter the first name")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter the last name")])
    email = StringField('Email', validators=[DataRequired("Please enter the email"), Email("Please enter the Email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter the password"), Length(min=6, message="Password must be 6 charcters or more")])
    submit = SubmitField('Sign up')

