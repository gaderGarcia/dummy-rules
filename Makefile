install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
lint:
	#pylint
	python -m mypy --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs rules/rule.py
metadata:
	#provides the metadata source of the functions
	python3 metadata.py
test:
	#test
build:
	#build container
deploy:
	#deploy commands
all: install format lint test build deploy