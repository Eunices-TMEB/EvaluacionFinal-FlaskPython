from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "juan": {"password": "admin", "tipo": "administrador"},
    "pepe": {"password": "user", "tipo": "usuario"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1Morado', methods=['GET', 'POST'])
def ejercicio1Morado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template('ejercicio1Morado.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=monto_descuento,
                               total_final=total_con_descuento,
                               mostrar_resultado=True)

    return render_template('ejercicio1Morado.html', mostrar_resultado=False)


@app.route('/ejercicio2Verde', methods=['GET', 'POST'])
def ejercicio2Verde():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['nombre']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario]['password'] == password:
            tipo = usuarios[usuario]['tipo']
            mensaje = f"Bienvenido {tipo} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2Verde.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True, port=5000)