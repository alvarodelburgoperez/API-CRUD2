import pytest
from app import app, db, Hidrosaurio  # Importa directamente si app.py está en la raíz del proyecto

import os

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

def test_create_and_index_hidrosaurio(client):
    # Crear un nuevo Hidrosaurio
    response = client.post('/create', data={
        'name': 'Hidrosaurio 1',
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    assert response.status_code == 302  # Verificar redirección después de crear

    # Verificar que el hidrosaurio aparece en la página de índice
    response = client.get('/')
    assert response.status_code == 200  # Verificar que la ruta funciona
    assert b'Hidrosaurio 1' in response.data  # Asegurarse de que el nombre del hidrosaurio está en la respuesta
