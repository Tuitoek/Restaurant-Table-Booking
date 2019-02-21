from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,TimeField
from wtforms.validators import Required
from wtforms.fields.html5 import DateField

class TableBookingForm(FlaskForm):
    entrydate = DateField('Check in',format='%Y-%m-%d',validators=[Required()])
    guests = StringField('Guest No.',validators=[Required()])
    adults = StringField('Adults No.',validators=[Required()])
    children = StringField('Children No.',validators=[Required()])
    submit = SubmitField('Submit')

class RestForm(FlaskForm):
    