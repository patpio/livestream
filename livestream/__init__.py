from flask_socketio import SocketIO

from flask import Flask

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    socketio.init_app(app)

    from livestream.views import bp_main
    app.register_blueprint(bp_main, url_prefix='/')

    from livestream.events.audience import bp_audience
    app.register_blueprint(bp_audience, url_prefix='/livestream')

    from livestream.events.commentator import bp_commentator
    app.register_blueprint(bp_commentator, url_prefix='/commentator')

    return app
