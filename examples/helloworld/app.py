from flask import Flask

app = Flask("myapp")

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route("/hello")
def hello2():
    return "<h1>Hello World</h1><p>This is a paragraph</p>"

app.run()