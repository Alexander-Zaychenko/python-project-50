install:
	pip install poetry && poetry install

test-coverage:
    poetry run pytest --cov=gendiff --cov-report xml