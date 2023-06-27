from flask import Flask, render_template, request, redirect, url_for
import database as db
app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def home():
    if request.method == 'POST':
        print("Pagina pasajero")
        return render_template("pasajeros.html")
    else:
        print("Pagina formulario")
        return render_template("formulario.html")


@app.route('/mostrar',methods=["POST","GET"])
def pasajero():
    if request.method == 'POST':
        cursor = db.DATABASE.cursor()
        cursor.execute("SELECT * FROM viajes")
        viajes = cursor.fetchall()
        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in viajes:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        print("Tome este camino")
        return render_template("pasajeros.html",viajes=insertObject)
    else:
        return render_template("pasajeros.html")


if __name__ == '__main__':
    app.run(debug="True")
