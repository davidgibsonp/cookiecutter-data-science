import webbrowser
import os

gitinit = input("git init? [y]es / [n]o: ") 
if gitinit.lower() == 'y':
	# gitinit
	print("\ninitialized git repo")
	os.system("git init")

	# open browser to create repo
	print("create remote Github repo")
	webbrowser.open('https://github.com/new', new=2)

	# add remote
	remote = input("enter remote origin: ") 
	os.system(f"git remote add origin {remote}")
	os.system(f"rm */.gitkeep")