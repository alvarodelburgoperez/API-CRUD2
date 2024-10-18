import unittest
from app import app, db, Hidrosaurio

class TestApp(unittest.TestCase):
    def setUp(self):
        # Configura una base de datos en memoria para pruebas
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def test_index(self):
        """Prueba que la página principal cargue correctamente."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_hidrosaurio(self):
        """Prueba la creación de un hidrosaurio."""
        response = self.app.post('/create', data={
            'name': 'Dino',
            'species': 'TRE',
            'weight': 100,
            'color': 'Green',
            'feeding': 'Carnivore'
        })
        self.assertEqual(response.status_code, 302)  # Redirecciona al index

    def tearDown(self):
        """Limpia la base de datos después de cada prueba."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()
