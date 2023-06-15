install:
	pip install --upgrade pip && pip install -r requirements.txt && touch __init__.py
format:
	black *.py
lint:
	python -m pylint ${PWD}
test:
	pytest test_functions.py
all: install format lint test