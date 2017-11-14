Package a project
=================

Your project should have the following structure:

```
[ProjectName]
  projectname
    - source code files
  - setup.py
  - ez_setup.py
  - README.rst
```

You can use the files in this directory, but make sure to customize ``setup.py``

File ``ez_setup.py`` should not be modified and is here to help with people who don't have setuptools already installed on their machine.

To upload to PyPI, first open an account on PyPI (or use the EGF account), then run this command:

```
sudo python3 setup.py sdist upload
```

Everytime you want to update the package, first increase the version number, then run the line above again.



Tips
----

- When developing the package, on your own computer, install the package with `python setup.py develop`, this way the package in installed "inplace" and any change you do to the source code of the package will take effect immediately.
- (VZ) on my computer I added the ``.pypirc`` file (with the right password) in my ``/home`` folder, not sure if strictly necessary.