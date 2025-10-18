# Makefile

.PHONY: test reset-db lint

test:
	pytest -v tests/

reset-db:
	flask reset-db

lint:
	flake8 app/ tests/

black-check:
	black --check .

black-format:
	black .
