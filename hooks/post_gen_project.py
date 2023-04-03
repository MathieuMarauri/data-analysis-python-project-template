import os
import subprocess

print("Installing the dependencies ...")
subprocess.call(["make", "install"])

print("Initializing a git repo ...")
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Setup project"])
subprocess.call(["pre-commit", "install"])
