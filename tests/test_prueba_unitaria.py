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

def test_create_hidrosaurio(client):
    response = client.post('/create', data={
        'name': 'Hidrosaurio 1',
        'species': 'H1',
        'weight': 100,
        'color': 'Verde',
        'feeding': 'Plantas'
    })
    assert response.status_code == 302  # Verificar redirección después de crear
    assert Hidrosaurio.query.count() == 1  # Verificar que se creó un hidrosaurio

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200  # Verificar que la ruta funciona
    assert b'Hidrosaurio' in response.data  # Asegurarse de que 'Hidrosaurio' está en la respuesta

def test_update_hidrosaurio(client):
    hidrosaurio = Hidrosaurio(name='Hidrosaurio 1', species='H1', weight=100, color='Verde', feeding='Plantas')
    db.session.add(hidrosaurio)
    db.session.commit()
    
    response = client.post(f'/update/{hidrosaurio.id}', data={
        'name': 'Hidrosaurio 1 actualizado',
        'species': 'H1',
        'weight': 150,
        'color': 'Azul',
        'feeding': 'Carnes'
    })
    assert response.status_code == 302  # Verificar redirección después de actualizar
    updated_hidrosaurio = Hidrosaurio.query.get(hidrosaurio.id)
    assert updated_hidrosaurio.name == 'Hidrosaurio 1 actualizado'  # Verificar que se actualizó correctamente

def test_delete_hidrosaurio(client):
    hidrosaurio = Hidrosaurio(name='Hidrosaurio 1', species='H1', weight=100, color='Verde', feeding='Plantas')
    db.session.add(hidrosaurio)
    db.session.commit()
    
    response = client.get(f'/delete/{hidrosaurio.id}')
    assert response.status_code == 302  # Verificar redirección después de eliminar
    assert Hidrosaurio.query.count() == 0  # Verificar que se eliminó el hidrosaurio
