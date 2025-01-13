from src import create_app
from src.extensions import login_manager

app = create_app()

login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
