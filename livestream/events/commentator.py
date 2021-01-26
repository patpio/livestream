from flask import Blueprint, session, url_for, render_template
from flask_socketio import join_room, emit
from werkzeug.utils import redirect

from livestream import socketio

bp_commentator = Blueprint('commentator', __name__)


@bp_commentator.route('/')
def stream():
    commentator = session.get('commentator', '')
    room = session.get('room', '')

    if commentator == '' or room == '':
        return redirect(url_for('main.home'))

    return render_template('commentator.html', commentator=commentator, room=room)


@socketio.on('joined', namespace='/commentator')
def handle_connect(connect):
    join_room(session.get('room', ''))


@socketio.on('message', namespace='/commentator')
def handle_message(message):
    room = session.get('room', '')
    print(message)
    emit('message', message, namespace='/livestream', broadcast=True, room=room)

# TODO do kazdej wiadomosci dodac godzine/minute, jak wpadnie bramka to ma sie pojawic emoji https://emojifinder.com/soccer