# #Building a web application with flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def hello():
    return render_template("form.html")

if __name__ == 'main':
    app.run(host='0.0.0.0', debug=True)