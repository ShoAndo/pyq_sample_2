from flask import Flask
app = Flask(__name__)

@app.route("/python")
def hello_world():
    return "Hello Sho Ando"

if __name__ == "__main__":
    app.run()