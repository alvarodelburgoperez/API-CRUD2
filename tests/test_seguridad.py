import pytest
from app import app, db, Hidrosaurio  # Importa directamente si app.py está en la raíz del proyecto


@pytest.fixture
def client():
    # Configurar la aplicación para pruebas
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()  # Crear tablas en memoria
        yield app.test_client()  # Proporcionar un cliente de prueba
        db.drop_all()  # Limpiar la base de datos después de las pruebas

def test_sql_injection(client):
    # Intentar inyección SQL a través de la entrada del usuario
    response = client.post('/create', data={
        'name': "'; DROP TABLE hidrosaurio; --",
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    # Verificar que la tabla aún existe
    assert Hidrosaurio.query.count() == 0  # La tabla no debe haber sido eliminada

def test_xss_protection(client):
    # Intentar inyectar un script a través de la entrada del usuario
    response = client.post('/create', data={
        'name': '<script>alert("XSS")</script>',
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    
    # Verificar que el contenido no incluye el script
    assert b'<script>' not in response.data  # El script no debe estar presente en la respuesta

def test_create_hidrosaurio_valid_data(client):
    # Prueba con datos válidos
    response = client.post('/create', data={
        'name': 'Hidrosaurio 1',
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    assert response.status_code == 302  # Verificar redirección después de crear
    assert Hidrosaurio.query.count() == 1  # Verificar que se creó un hidrosaurio


def test_sql_injection(client):
    # Intentar inyección SQL a través de la entrada del usuario
    response = client.post('/create', data={
        'name': "'; DROP TABLE hidrosaurio; --",
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    assert response.status_code == 400  # Esperar un código de error (Bad Request)

    # Asegurarse de que no se haya creado un hidrosaurio con el nombre malicioso
    with app.app_context():
        count = Hidrosaurio.query.filter_by(name="'; DROP TABLE hidrosaurio; --").count()
        assert count == 0  # No se debe haber agregado


