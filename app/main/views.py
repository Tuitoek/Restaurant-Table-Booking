from flask import render_template,url_for,redirect,flash
from . import main
# from flask_login import login_required,current_user
from ..models import Book
from .forms import BookForm

#Views
@main.route('/',methods= ['POST', 'GET'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/booking',methods=['POST','GET'])
def booking():
    '''
    View page function that returns the book page and its data
    '''
    book_form = BookForm()
    if book_form.validate_on_submit():
        adults= book_form.adults.data
        date = book_form.date.data
        resname=book_form.resname.data
        restype=book_form.restype.data
        children = book_form.children.data

        db.session.add(booking)
        db.session.commit()

        flash(f' Hi {{user.username}} Your Reservation has been made!')

        return redirect(url_for('main.index'))

    return render_template('booking.html',book_form=book_form)
