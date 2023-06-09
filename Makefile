install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff -h

test:
	pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
