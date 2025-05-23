from flask import Flask
from contact.routes import contact_bp

app = Flask(__name__)
app.register_blueprint(contact_bp)

if __name__ == '__main__':
    app.run(debug=True)