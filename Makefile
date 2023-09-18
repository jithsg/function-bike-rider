install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C,W1203,W1202 hello.py hello_cli.py
format:
	black *.py
test:
	python -m pytest -vv --cov=hello test_hello.py
all: install lint format