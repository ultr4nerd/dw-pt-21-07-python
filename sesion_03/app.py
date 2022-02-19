import random
from flask import Flask

app = Flask(__name__)

@app.route("/hola-flask")
def hola_flask():
    number = random.randint(0, 11)
    return f"<h1>Hola, Flask</h1>"
