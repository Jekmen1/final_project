from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ...models.chat import ChatRoom, Message
from ...extensions import db
from flask_socketio import emit, join_room, leave_room
from ...extensions import socketio

chat_bp = Blueprint('chat', __name__, template_folder='templates')


@chat_bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        room_name = request.form['room_name']
        if not ChatRoom.query.filter_by(name=room_name).first():
            new_room = ChatRoom(name=room_name)
            db.session.add(new_room)
            db.session.commit()
        return redirect(url_for('chat.room', room_name=room_name))

    rooms = []
    for room in ChatRoom.query.all():
        last_message = Message.query.filter_by(room_id=room.id).order_by(Message.timestamp.desc()).first()
        rooms.append({
            "room": room,
            "last_message": last_message.content if last_message else "No messages yet."
        })

    return render_template('chatapp/chat.html', rooms=rooms)


@chat_bp.route('/chat/<room_name>')
@login_required
def room(room_name):
    all_rooms = ChatRoom.query.all()
    room = ChatRoom.query.filter_by(name=room_name).first_or_404()
    messages = Message.query.filter_by(room_id=room.id).order_by(Message.timestamp).all()
    return render_template('chatapp/room.html', rooms=all_rooms, room=room, messages=messages)



@socketio.on('send_message')
def handle_send_message(data):
    room = data['room']
    message = Message(
        user_id=current_user.id,
        room_id=data['room_id'],
        content=data['message']
    )
    db.session.add(message)
    db.session.commit()
    emit('receive_message', {
        'username': current_user.username,
        'message': data['message']
    }, room=room)

@socketio.on('join')
def handle_join(data):
    join_room(data['room'])
    emit('status', {'msg': f"{current_user.username} has joined the room."}, room=data['room'])

@socketio.on('leave')
def handle_leave(data):
    leave_room(data['room'])
    emit('status', {'msg': f"{current_user.username} has left the room."}, room=data['room'])