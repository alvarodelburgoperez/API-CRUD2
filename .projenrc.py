from projen.python import PythonProject

project = PythonProject(
    author_email="alvarodelburgoperez@gmail.com",
    author_name="Álvaro",
    module_name="entorno_api",
    name="entorno_api",
    version="0.1.0",
)

project.synth()