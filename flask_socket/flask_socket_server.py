from flask import Flask, render_template, request
from flask_socketio import SocketIO
from requests import get
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.jinja_env.auto_reload = True

socketio = SocketIO(app)


@app.route('/')
def index():
   # return render_template('index.html',data=send)
    return render_template('index_server.html')


@app.route('/send_all')
def send_all():
    """
    广播
    :return: 
    """
    message = request.args.get('message')

    socketio.emit('get',message)

    return {'status': 'ok'}

"""
@app.route('/send')
def send_message():
    
    单独发送
    :return:

    sid = request.args.get('sid')
    message = request.args.get('message')

    socketio.send(message, to=sid)

    return {'status': 'ok'}"""


@socketio.on('connect')
def connect():
    print('connect')
    socketio.send({'sid': request.sid})


@socketio.on('disconnect')
def disconnect():
    print('disconnect')


@socketio.on('message')
def handle_message(data):
    print(data)
    socketio.send( data)


if __name__ == '__main__':
    
    socketio.run(app,port=3000, debug=True)
