from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect

class FormularioAgregar(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    time = IntegerField('time', validators=[DataRequired(), NumberRange(min=0, max=100)])

app = Flask("myapp")
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "asdasdasd"

competidores = []

@app.route("/")
def index():
    return "Soy la pag principal"

@app.route("/lista")
def lista():
    return render_template("lista.html", corredores=competidores)

@app.route("/agregar", methods=["GET", "POST"])
def hello2():
    form = FormularioAgregar()
    if form.validate_on_submit():
        competidor = {
            'nombre': request.form["materia"],
            'tiempo': request.form["time"],
        }
        competidores.append(competidor)
        print(competidores)
        return redirect("/lista")
    else:
        print("Recibi un get!!!")
        return render_template("agregar.html", form=form)

app.run()