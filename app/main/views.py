from flask import render_template,url_for,redirect,flash
from . import main
# from flask_login import login_required,current_user
from ..models import Book
from .forms import BookForm
from .. import db

#Views
@main.route('/',methods= ['POST', 'GET'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/book',methods=['POST','GET'])
def book():
    '''
    View page function that returns the book page and its data
    '''
    book_form = BookForm()
    if book_form.validate_on_submit():
        adult= book_form.adult.data
        date = book_form.date.data
        resname=book_form.resname.data
        restype=book_form.restype.data
        children = book_form.children.data

        book = Book(adult = book_form.adult.data,date = book_form.date.data,resname = book_form.resname.data
,restype = book_form.restype.data,children = book_form.children.data)
        db.session.add(book)
        db.session.commit()

        flash(f' Hi Tuitoek Your Reservation has been made!')

        return redirect(url_for('main.index'))

    return render_template('booking.html',book_form=book_form)

    
