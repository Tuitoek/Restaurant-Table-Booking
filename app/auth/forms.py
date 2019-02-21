from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo,Length
from ..models import User

class RegisterForm(FlaskForm):
    email = StringField('Enter your email address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required(),Length(min=5,max=25)])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match'),Length(min=8,max=25)])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required(),Length(min=2,max=25)])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
