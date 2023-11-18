from flask import Flask
from Controllers.MainController import main_controller_app

app = Flask(__name__)

app.register_blueprint(main_controller_app)

if __name__ == "__main__":
    app.run()
