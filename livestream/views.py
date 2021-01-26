from flask import Blueprint, render_template, session, url_for
from werkzeug.utils import redirect

from livestream.forms import UserForm, CommentatorForm

bp_main = Blueprint('main', __name__)


@bp_main.route('/', methods=['GET', 'POST'])
def home():
    user_form = UserForm()
    if user_form.validate_on_submit():
        session['username'] = user_form.username.data
        session['room'] = user_form.room.data
        return redirect(url_for('audience.stream'))

    admin_form = CommentatorForm()
    if admin_form.validate_on_submit():
        session['commentator'] = admin_form.admin.data
        session['room'] = admin_form.room.data
        return redirect(url_for('commentator.stream'))
    return render_template('home.html', user_form=user_form, admin_form=admin_form)
