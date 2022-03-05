import random

from flask import Flask, render_template, request

from forms import UserForm


app = Flask(__name__)
app.config["ENV"] = "development"
app.config["SECRET_KEY"] = "asgdhjaklsdas"


@app.route("/")
def index():
    number = random.randint(0, 10)
    return render_template("index.html", number=number)


@app.route("/perfil/<username>")
def perfil(username):
    return f"@{username}"


@app.route("/crear", methods=["GET", "POST"])
def crear_usuario():
    # Técnicas de debugging
    # breakpoint()  # Python >= 3.7
    # import pdb; pdb.set_trace()  # Python < 3.7
    # print(f"{form=}")  # Imprimir valores de variable 

    # Versión sin WTForms
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['contrasena ']
    #     print(username, password)

    # Versión corta 
    # if form.validate_on_submit():
    #     return f"Bien hecho, {form.username.data}"

    form = UserForm()
    if request.method == 'POST' and form.validate():
        form.save()
        return f"Bien hecho, {form.username.data}"
    return render_template("usuario.html", form=form)


@app.route('/parametros')
@app.route('/parametros/<nombre>')
@app.route('/parametros/<nombre>/<int:edad>')
def recibe_parametros(nombre="humano", edad=0):
    return ("nombre   {}\n edad    {} años".format(nombre, edad))


@app.route("/calculadora/v2/<int:n1>/")
def calculadora_v2(n1):
    resultado = 0
    return "El resultado es {}".format(resultado)


@app.route("/calculadora")
def calculadora():
    n1 = int(request.args.get('n1', '0'))
    n2 = int(request.args.get('n2', '0'))
    operacion = request.args.get('operacion')
    resultado = 0

    if operacion == 'suma':
        resultado = n1 + n2
    elif operacion == 'resta':
        resultado = n1 - n2
    elif operacion == 'multiplicacion':
        resultado = n1 * n2
    elif operacion == 'division':
        resultado = n1 // n2
    elif operacion == 'residuo':
        resultado = n1 % n2
    elif operacion == 'potencia':
        resultado = n1 ** n2

    return "El resultado es {}".format(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
