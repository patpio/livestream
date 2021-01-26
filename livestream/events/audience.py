from flask import Blueprint, session, url_for, render_template
from flask_socketio import join_room
from werkzeug.utils import redirect

from livestream import socketio

bp_audience = Blueprint('audience', __name__)


@bp_audience.route('/')
def stream():
    username = session.get('username', '')
    room = session.get('room', '')

    if username == '' or room == '':
        return redirect(url_for('main.home'))

    return render_template('audience.html', username=username, room=room)


@socketio.on('joined', namespace='/livestream')
def handle_connect(connect):
    print(connect)
    join_room(session.get('room', ''))
