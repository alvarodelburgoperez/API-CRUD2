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

encrypt:
	sops --encrypt --pgp <PGP_KEY_ID> secrets.yaml > secrets.enc.yaml

decrypt:
	sops --decrypt secrets.enc.yaml > secrets.yaml
