.DEFAULT_GOAL := help
.PHONY: help setup format lint

help:
	@echo "Make sure you have poetry installed"
	@echo "If this is the first time that you run this project, please run "make setup" prior to any action"
	@echo "setup: install the dependencies using poetry and the pre-commit hook"
	@echo "format: format the code, in python scripts and notebooks"
	@echo "lint: lint the code, in python scripts and notebooks"

setup:
	poetry install
	pre-commit install

format:
	nbqa black *.ipynb
	nbqa isort *.ipynb
	black *.py
	isort *.py

lint:
	nbqa flake8 *.ipynb
	flake8 *.py