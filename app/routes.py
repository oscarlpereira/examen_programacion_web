from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    precio =  9000
    nombre = total = descuento = total_a_pagar = None

    def descuento_edad (edad):
        if 18 <= edad <= 30:
            return 0.15
        elif edad > 30:
            return 0.25
        return 0


    def total_sin_descuento(cantidad, precio):
        return cantidad * precio


    def calculo_descuento(total, porcentaje):
        return total * porcentaje


    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad_tarros"])

        total= total_sin_descuento(cantidad, precio)
        porcentaje = descuento_edad(edad)
        descuento = calculo_descuento(total, porcentaje)
        total_a_pagar = total - descuento

    return render_template(
        "ejercicio1.html",
        nombre=nombre,
        total=total,
        descuento=descuento,
        total_a_pagar=total_a_pagar,
        )

@main.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    admin1 = "juan"
    contrasena1 = "admin"
    admin2 = "pepe"
    contrasena2 = "user"

    acceso = None
    usuario = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if (usuario == admin1 and contrasena == contrasena1) or \
           (usuario == admin2 and contrasena == contrasena2):
            acceso = True
        else:
            acceso = False
    return render_template("ejercicio2.html", acceso=acceso, usuario=usuario)

