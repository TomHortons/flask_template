<h2 align="center">Flask Template</h2>

## Installation and running tests
---
This is a flask-template with extentions of **Flask-Restful** and **JWT**.
Make sure you are using python3.6 or higher.

This template includes following coding supports.

* **test**: flask-pytest, flask-mock
* **formatter**: black (PEP8)
* **checker**: flake8
* **docStrings**: Google Python Style Guide
* coding style pre-commit hook

### Installation
---

Initialize your environment using virtualenv.
```
$ virtualenv --python python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Install coding style pre-commit.
```
$ pre-commit install
```

### Running tests
---

The simplest way to run tests:

```
python -m tests
```

To run a single test:

```
python -m tests tests/unit/test_unit.py::TestFirstUnit
```
