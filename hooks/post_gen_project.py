import os

os.system("make install")
os.system("git init")
os.system("git add .")
os.system("git commit -m 'Setup project'")
os.system("find . -type f -name '.gitkeep' -delete")
