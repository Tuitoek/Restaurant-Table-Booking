from flask import render_template,url_for,redirect,flash,request,abort
from . import main
from flask_login import login_required,current_user
from ..models import Book,User
from .forms import BookForm,UpdateProfile
from .. import db,photos


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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST','GET'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return redirect(url_for('main.update_pic',uname=uname))

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.profile_pic_path = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
