from flask import Flask, request, redirect, url_for, render_template, abort, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo para Hidrosaurios
class Hidrosaurio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(3), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    feeding = db.Column(db.String(80), nullable=False)

# Crear las tablas en la base de datos
def create_tables():
    with app.app_context():
        db.create_all()  # Asegúrate de que esto se ejecute en el contexto de la aplicación

# Llama a la función para crear tablas antes de ejecutar la aplicación
create_tables()

# Ruta principal - Mostrar todos los registros (Read)
@app.route('/')
def index():
    hidrosaurios = Hidrosaurio.query.all()  # Obtén todos los hidrosaurios desde la base de datos
    return render_template('index.html', hidrosaurios=hidrosaurios)

# Ruta para agregar un nuevo registro (Create)
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        weight = request.form['weight']
        color = request.form['color']
        feeding = request.form['feeding']

        # Validación básica: Evitar caracteres sospechosos en el nombre
        if ';' in name or '--' in name or len(name.strip()) == 0:
            flash("Nombre no válido. Intente nuevamente.", "error")
            abort(400)  # Retorna un código de error 400 (Bad Request)

        # Crear y almacenar el nuevo Hidrosaurio si pasa las validaciones
        new_hidrosaurio = Hidrosaurio(
            name=name, species=species, weight=weight, color=color, feeding=feeding
        )
        db.session.add(new_hidrosaurio)
        db.session.commit()

        return redirect(url_for('index'))  # Redirigir a la página principal
    
    return render_template('create.html')

# Ruta para actualizar un registro existente (Update)
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    hidrosaurio = db.session.get(Hidrosaurio, id)  # Cambiar a db.session.get()
    if hidrosaurio is None:
        abort(404)  # Si no se encuentra el hidrosaurio, abortar con un error 404

    if request.method == 'POST':
        hidrosaurio.name = request.form['name']
        hidrosaurio.species = request.form['species']
        hidrosaurio.weight = request.form['weight']
        hidrosaurio.color = request.form['color']
        hidrosaurio.feeding = request.form['feeding']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', hidrosaurio=hidrosaurio)

# Ruta para eliminar un registro (Delete)
@app.route('/delete/<int:id>')
def delete(id):
    hidrosaurio = db.session.get(Hidrosaurio, id)  # Cambiar a db.session.get()
    if hidrosaurio is None:
        abort(404)  # Si no se encuentra el hidrosaurio, abortar con un error 404

    db.session.delete(hidrosaurio)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        create_tables()  # Crear tablas solo si el archivo no existe
    app.run(debug=True)
