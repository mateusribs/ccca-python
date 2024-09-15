.PHONY: install test format
SHELL := /bin/bash
.ONESHELL:

install:
	@uv sync

test:
	@uv run python -m pytest -s -x --cov=src -vv

format:
	@uv run python -m ruff check . --fix
	@uv run python -m ruff format .

lint:
	@uv run python -m ruff check .
	@uv run python -m ruff check . --diff