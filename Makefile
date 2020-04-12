run:
	export FLASK_APP=app.py && export FLASK_ENV=development && ./venv/bin/flask run

install:
	rm -rf venv
	virtualenv venv -p /usr/bin/python3
	./venv/bin/pip install -r requirements.txt

test:
	curl -X POST -F 'text=bonjour gwenael' -F 'prefix=message' -F 'lang=fr' http://localhost:5000/speak