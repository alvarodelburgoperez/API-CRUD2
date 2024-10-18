import pytest
from app import app, db, Hidrosaurio  # Importa directamente si app.py está en la raíz del proyecto


@pytest.fixture
def client():
    # Configurar la aplicación para pruebas
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
        yield app.test_client()  # Proporcionar un cliente de prueba
        db.drop_all()  # Limpiar la base de datos después de las pruebas

def test_create_and_display_hidrosaurio(client):
    # Crear un nuevo Hidrosaurio
    response = client.post('/create', data={
        'name': 'Hidrosaurio Funcional',
        'species': 'H2',
        'weight': 120,
        'color': 'Rojo',
        'feeding': 'Carnes'
    })
    assert response.status_code == 302  # Verificar redirección después de crear

    # Asegurarse de que el Hidrosaurio se haya agregado a la base de datos
    hidrosaurio = Hidrosaurio.query.filter_by(name='Hidrosaurio Funcional').first()
    assert hidrosaurio is not None  # Verificar que el hidrosaurio fue creado

    # Verificar que se muestre en la página principal
    response = client.get('/')
    assert response.status_code == 200  # Verificar que la ruta funciona
    assert b'Hidrosaurio Funcional' in response.data  # Verificar que el nombre aparece en la respuesta
