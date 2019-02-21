from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,Length
from wtforms.fields.html5 import DateField
from ..models import Book

class BookForm(FlaskForm):
      adults = StringField('Enter your email address',validators=[Required()])
      date = DateField("Enter reservation date",format='%Y-%m-%d',validators=[Required()])
      resname = StringField('Enter your username',validators = [Required(),Length(min=5,max=25)])
      restype =StringField("Enter the reservation type",validators=[Required()])
      children = PasswordField('Confirm Passwords',validators = [Required(),Length(min=2,max=6)])
      submit = SubmitField('Reseve')
