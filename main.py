from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    sum == 1 + 1
    return "Hello World!" + str(sum)


if __name__ == "__main__":
    app.run()
