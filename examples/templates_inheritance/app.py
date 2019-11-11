from flask import Flask, render_template

app = Flask("myapp")

@app.route("/")
@app.route("/doc1")
def doc1():
    return render_template("document1.html")

@app.route("/doc2")
def doc2():
    return render_template("document2.html")

app.run()