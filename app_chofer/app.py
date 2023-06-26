from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de pasajeros disponibles (solo para ejemplo)
pasajeros_disponibles = [
    {'nombre': 'Pasajero 1', 'destino': 'Destino 1', 'telefono': '123456789'},
    {'nombre': 'Pasajero 2', 'destino': 'Destino 2', 'telefono': '987654321'},
    {'nombre': 'Pasajero 3', 'destino': 'Destino 3', 'telefono': '555555555'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_chofer = request.form['nombre']
        patente_vehiculo = request.form['patente']
        asientos_disponibles = request.form['asientos']
        lugar_estacionamiento = request.form['lugar_estacionamiento']

        return render_template('pasajeros.html', pasajeros=pasajeros_disponibles,
                               nombre_chofer=nombre_chofer, patente_vehiculo=patente_vehiculo,
                               asientos_disponibles=asientos_disponibles,
                               lugar_estacionamiento=lugar_estacionamiento)
    
    return render_template('formulario.html')

@app.route('/pasajero/<nombre>', methods=['GET'])
def ver_pasajero(nombre):
    pasajero = None
    for p in pasajeros_disponibles:
        if p['nombre'] == nombre:
            pasajero = p
            break
    
    return render_template('detalle_pasajero.html', pasajero=pasajero)

@app.route('/confirmar', methods=['POST'])
def confirmar_pasajero():
    nombre_pasajero = request.form.get('pasajero')
    # Lógica para confirmar al pasajero
    return redirect('/')

@app.route('/rechazar', methods=['POST'])
def rechazar_pasajero():
    nombre_pasajero = request.form.get('pasajero')
    # Lógica para rechazar al pasajero
    return redirect('/')

if __name__ == '__main__':
    app.run()
