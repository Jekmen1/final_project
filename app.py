from src import create_app
from src.extensions import login_manager, socketio


app = create_app()

login_manager.init_app(app)

if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
