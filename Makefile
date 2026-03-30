.PHONY: lint test typecheck format all

lint:
	uv run ruff check src/ tests/


format:
	uv run ruff format src/ tests/


test:
	uv run pytest tests/ -v


typecheck:
	uv run mypy src/


all: lint typecheck test
