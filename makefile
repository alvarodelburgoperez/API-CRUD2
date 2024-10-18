install:
    pip install -r requirements.txt

lint:
    pylint app.py

test:
    coverage run -m unittest discover

coverage-report:
    coverage report -m

vuln-scan:
    trivy filesystem .
