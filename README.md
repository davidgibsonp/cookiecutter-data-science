# Cookiecutter Data Science

My personal simplified version of [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/).

**Key differences:**

- Reduced total files generated 
- Option to initialize git repo

### Requirements
[cookiecutters](http://cookiecutter.readthedocs.org/en/latest/installation.html) is a python command-line utility that creates projects from templates.

```sh
pip install cookiecutter
```

### Run
In terminal simply run the following command and enter the user prompts. I recommend creating an alias of the command for future use.

```sh
cookiecutter https://github.com/davidgibsonp/cookiecutter-data-science
```


### Result
The above commanad will create the following directory structure. 

```
.
├── .git
├── .gitattributes
├── .gitignore
├── LICENSE
├── R
├── README.md
├── data
│   ├── processed
│   └── raw
├── docs
├── notebooks
├── reports
├── requirements.txt
├── setup.py
└── src
    └── __init__.py
```