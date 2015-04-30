from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def say_hi():
    return "Hello World"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
