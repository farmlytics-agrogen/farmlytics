from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Farmlytics AI Server Running"

if __name__ == "__main__":
    app.run()
