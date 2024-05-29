.DEFAULT_GOAL := help
.PHONY: help

help:
	@echo "Make sure you have poetry installed"
	@echo "If this is the first time that you run this project, please run "make install" prior to any action"

setup:
	poetry install
	pre-commit install

format-notebook:
	nbqa black *.ipynb
	nbqa isort *.ipynb