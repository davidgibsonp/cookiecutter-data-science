# Cookiecutter Data Science

My personal simplified version of [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/davidgibsonp/cookiecutter-data-science

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
.
├── .gitattributes
├── .gitignore
├── LICENSE
├── Makefile
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