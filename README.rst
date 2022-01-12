***********************
Template Python Package
***********************

Description of the Repository:
==============================

This is a simple template for a python package development repository. The project
defines ``setup.py`` and ``pyproject.toml`` with all the standard configuration one
might want for a python package development, such as unit testing with ``pytest``
(including docstring and documentation testing and coverage), code formatting by
``black`` and testing on a matrix of python versions and dependency versions powered
by ``tox``.

The package source code is structured in the ``src`` directory, which means that
the package needs to be ``pip installed`` to run tests and development, which appears
to be an agreed upon best practice for package development.

A full CI/CD pipeline is implemented via *GitHub Actions*, which performs on any push
to ``master`` branch the following:

* Check if the project code is ``black``-formatted.
* Run all the tests with ``pytest`` and ``tox`` on a matrix of supported python versions
  and dependency versions.
* If the commit is tagged, publish the package to PyPI
  * TestPyPI is used in this template.
  * The package only gets published if ``twine check dist/*`` executes successfully.
  * The package only gets published if tests run successfully and the code is formatted.


README Template:
================

Installation:
-------------

The ``pkg-template-mh`` package can be installed either from PyPI

.. code-block:: bash

    python3 -m pip install pkg-template-mh

or from the GitHub_ page

.. code-block:: bash

    python3 -m pip install git+https://github.com/hanicinecm/template-python-package.git


For Developers:
---------------
It goes without saying that any development should be done in a clean virtual
environment.
After cloning or forking the project from its GitHub_ page, ``pkg-template-mh`` can be
installed into the virtual environment in the editable mode by running

.. code-block:: bash

    pip install -e .[dev]


The ``[dev]`` extra installs (apart from the package dependencies) also several
development-related packages, such as ``pytest``, ``black``, or ``tox``.
The tests can then be executed by running (from the project root directory)

.. code-block:: bash

    pytest --cov


The project does not have the ``requirements.txt`` file by design, as all the package
dependencies are rather handled by the ``setup.py``.
The package therefore needs to be installed locally to run the tests, which grants the
testing process another layer of usefulness.

Docstrings in the project adhere to the `Google Python Style Guide`_.
The project code is formatted by ``black``.
Always make sure to format your code before submitting a pull request, by running
``black`` on all your python files.


Examples:
---------

.. code-block:: pycon

    >>> print("hello, world!")
    hello, world!

    >>> from pkg_template.module import get_dataframe
    >>> get_dataframe((2, 3))
       a  b  c
    0  0  1  2
    1  3  4  5


.. _ExoMol: https://www.exomol.com/
.. _GitHub: https://github.com/hanicinecm/template-python-package
.. _Google Python Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings