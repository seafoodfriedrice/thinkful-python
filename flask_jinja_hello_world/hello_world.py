from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def say_hi():
    return render_template('hello.html', title='Hello World Page')

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_person.html', title='Hello {}'.format(name),
                           name=name.title())

@app.route("/jedi/<first>/<last>")
def make_jedi_name(first, last):
    jedi_name = last[0:3] + "'" + first[0:2]
    return render_template('jedi.html', title='Jedi Name',
                           jedi_name=jedi_name.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
