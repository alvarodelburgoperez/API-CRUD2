from locust import HttpUser, between, task
from app import app, db, Hidrosaurio  # Importa directamente si app.py está en la raíz del proyecto


class HidrosaurioUser(HttpUser):
    wait_time = between(1, 5)  # Espera entre 1 y 5 segundos entre tareas

    @task
    def index(self):
        self.client.get("/")  # Realiza una solicitud GET a la ruta principal

    @task
    def create_hidrosaurio(self):
        # Realiza una solicitud POST para crear un nuevo Hidrosaurio
        self.client.post("/create", data={
            'name': 'Hidrosaurio Test',
            'species': 'H1',
            'weight': 100,
            'color': 'Verde',
            'feeding': 'Plantas'
        })

    @task
    def update_hidrosaurio(self):
        # Supongamos que hay un Hidrosaurio con ID 1
        self.client.post("/update/1", data={
            'name': 'Hidrosaurio Actualizado',
            'species': 'H1',
            'weight': 150,
            'color': 'Rojo',
            'feeding': 'Carne'
        })

    @task
    def delete_hidrosaurio(self):
        # Supongamos que hay un Hidrosaurio con ID 1
        self.client.get("/delete/1")  # Realiza una solicitud GET para eliminar un Hidrosaurio
