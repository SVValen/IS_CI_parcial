from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola profeee :))))))"

if __name__ == "__main__":
    app.run()