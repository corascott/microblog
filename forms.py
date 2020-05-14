from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    """description of class"""
    username = StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class Profile():
    eeheife



class RegistrationForm(FlaskForm):
    """user registration form"""
    newusername = StringField('Enter Username', validators=[DataRequired()])
    newpassword = StringField('Enter Password', validators=[DataRequired()])
    newemail = StringField('Enter Email', validators=[DataRequired(), Email()])
    passwordCheck = StringField('Re-enter Password', validators=[DataRequired(), EqualTo('newpassword')])
    submit = SubmitField('Create Account')
    
    def validate_username(self, newusername):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a differnt username.')

    def validate_email(self,newemail):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a differnt email.')