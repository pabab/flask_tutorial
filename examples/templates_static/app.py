from flask import Flask, render_template

app = Flask("myapp")

@app.route("/")
def hello():
    return render_template("hello.html", nombre="Pablo")

app.run()