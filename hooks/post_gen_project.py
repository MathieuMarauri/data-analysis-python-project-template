import os

python_version = "{{cookiecutter.python}}"

os.system("pyenv local " + python_version)
os.system("poetry env use " + python_version)
os.system("poetry self add poetry-plugin-up")
os.system("poetry up --latest")
os.system("git init")
os.system("git add .")
os.system("git commit -m 'Setup project'")
os.system("pre-commit install")
os.system("find . -type f -name '.gitkeep' -delete")
