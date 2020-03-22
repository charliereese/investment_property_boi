# Description

investment-property-boi is a python package for calculating monthly investment property cash flows and holding period returns.

# Usage

```
pip install investment-property-boi

...

# TBU
```

# Appendix

### Creating a build

First, update the version number in setup.py.

Then, in the root folder:

`python setup.py sdist bdist_wheel`

In the root folder:

### Uploading a build

Prod:
`python -m twine upload dist/*`

Test:
`python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

### Installing the package

See https://packaging.python.org/tutorials/packaging-projects/

### Useful information for building packages:

- [what is __init__.py for](https://stackoverflow.com/questions/448271/what-is-init-py-for)

### Running test suite

`python -m unittest discover tests`
