from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo,Length
from wtforms.fields.html5 import DateField
from ..models import Book,User

class BookForm(FlaskForm):
      adult = StringField('Enter the number of adults',validators=[Required()])
      date = DateField("Enter reservation date",format='%Y-%m-%d',validators=[Required()])
      resname = StringField('Enter your username',validators = [Required(),Length(min=5,max=25)])
      restype =StringField("Enter the reservation type",validators=[Required()])
      children = StringField('Enter the number of children',validators = [Required(),Length(min=2,max=6)])
      submit = SubmitField('Reseve')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    

