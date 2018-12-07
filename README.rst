ipgdrive
########
|PyPI-Status| |PyPI-Versions| |LICENCE|

A service that writes the public ip address of the host computer to a file on Google Drive.

.. code-block:: python

  # after setting up ~/.config/ipgdrive/cfg.json
  # setup a cronjob to write the public ip address to 
  # Google doc every 5 minutes
  ipgdrive setupjob -m 5

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install ipgdrive


Setup
=====

To enable Google Drive access, follow the `instructions here <https://gspread.readthedocs.io/en/latest/oauth2.html>`_ to create a service account with Google Drive access, and create a json key file for it.

Don't forget to follow all the above instructions, including sharing your spreadsheet with an email you have in your ``json_key['client_email']`` (Otherwise you’ll get a ``SpreadsheetNotFound`` or an ``APIError`` with ``"PERMISSION_DENIED"`` exception when trying to open it).

Place this file in the ``~/.config/ipgdrive/`` folder, and rename it to ``google_drive_service_account_key.json``.

Additionally, create a ``cfg.json`` file inside the ``~/.config/ipgdrive/`` folder, and populate it with the following values:

.. code-block:: json

    {
        "spreadsheet_name": "my_server_public_ip",
        "username": "momo",
        "freq_minutes": 5
    }

The username is for the user running the process on the server, NOT the Google account username.


Use
===

.. code-block:: python

  # after setting up ~/.config/ipgdrive/cfg.json
  # setup a cronjob to write the public ip address to 
  # Google doc every 5 minutes
  ipgdrive setupjob -m 5


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/ipgdrive.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd ipgdrive
  pip install -e '.[test]'


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd ipgdrive
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/ipgdrive.svg
  :target: https://pypi.python.org/pypi/ipgdrive

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/ipgdrive.svg
   :target: https://pypi.python.org/pypi/ipgdrive

.. |Build-Status| image:: https://travis-ci.org/shaypal5/ipgdrive.svg?branch=master
  :target: https://travis-ci.org/shaypal5/ipgdrive

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
  :target: https://github.com/shaypal5/ipgdrive/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/ipgdrive/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/ipgdrive?branch=master
