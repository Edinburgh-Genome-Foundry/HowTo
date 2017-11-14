Create a test suite (with pytest)
=================================


Your project should have the following structure:

```
|-- ProjectName
    +-- projectname
    |   +-- source_file1.py
    |   +-- source_file2.py
    +-- tests
    |   +-- test_basics.py
    |   +-- test_other.py
    +-- README.md
    +-- etc.
```

Files in the ``test`` folder can be called anything as long as they start with ``test``. See ``test_basics.py`` for an example of such file.

then install ``pytest`` with
```
pip install pytest
```

From folder ``ProjectName``, run the test suite with:

```
python3 -m pytest
```

Running test suites on travis.ci
--------------------------------

- Add the ``.travis.yml`` file at the root of your python package (same level as the README).
- Push your package on github
- Open an account on [https://travis-ci.org/](https://travis-ci.org/), which will be linked to your Github account.
- In travis, activate the Github repository with your python package.

Travis will run the test suite every time you push to the repo and send you emails if things get broken or fixed. You can also add the following code to your README to add the status badge:

[![Build Status](https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver.svg?branch=master)](https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver)

```
Markdown:
[![Build Status](https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver.svg?branch=master)](https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver)

RST:
.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver.svg?branch=master
    :target: https://travis-ci.org/Edinburgh-Genome-Foundry/DnaWeaver
```

