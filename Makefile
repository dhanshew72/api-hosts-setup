ACTIVATE_VENV=. .venv/bin/activate

dev-env: clean
	python3.10 -m venv .venv
	$(ACTIVATE_VENV); pip3 install -r requirements.txt

config:
	cp config.tmpl.yaml src/config.yaml
	yq -e -i '.host_data.api_key = "${API_KEY}"' config.yaml

clean:
	rm -rf .venv

run:
	$(ACTIVATE_VENV); PYTHONPATH=src python3.10 src/main.py

run-db:
	docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server:6.0-ubi8

stop-db:
	docker stop mongodb
	docker rm mongodb
