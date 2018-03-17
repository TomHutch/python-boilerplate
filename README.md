Python Boilerplate
==============

This is a Python project boilerplate, to be used as a reference or as a seed for a new project.
It uses direnv to manage the environment change upon moving into the project directory.
The project structure is set up to work with Pybuilder and PyCharm.

## Initial Setup

```bash
git clone git@github.com:TomHutch/python-boilerplate.git <dirname>
cd <dirname>
rm -rf .git && git init
pip install pybuilder
direnv allow
pyb
```

## Pycharm Setup

* Mark the `src/main/python` directory as sources root
* Check the project Python interpreter is set correctly in preferences to use the python binary in the `.direnv` directory
