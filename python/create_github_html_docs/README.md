# Create HTML docs hosted on GitHub for your Python package

## Using Sphinx to GitHub Pages V3 GitHub Action

In this approach, we generate the documentation from docstrings and rst template ("instruction") files. The documentation that is displayed on github.io is automatically generated upon creating a package release. See workflow steps below.

**Write your docstrings in a suitable format**

For example, use the `numpydoc` format.


**Install Sphinx and required themes**
```
pip install -U sphinx
pip install sphinx_rtd_theme
pip install sphinx-press-theme
```

**Set up the documentation sources**
```
cd /path/to/pkg/
mkdir docs
cd docs
sphinx-quickstart
```

**Edit the conf.py and the index.rst file**

Set `project`, `copyright`, `author`, and `extensions`, `html_theme` variables.
Set `napoleon_numpy_docstring = True` if using numpydoc style.
Create a `ref.rst` file with instructions to auto-generate the API reference from the docstrings.
See an example in [Minotaor's](https://github.com/Edinburgh-Genome-Foundry/Minotaor) `docs` directory.
In this package's index.rst, we include a link to the main readme (and the API reference), instead of duplicating the documentation.


**Build the documentation**

Issue this command from the `docs` directory:
```
make html
```
Check that everything looks nice.


**Set up the Github Actions workflow**

Use the "[Sphinx to GitHub Pages V3](https://github.com/marketplace/actions/sphinx-to-github-pages)" GitHub Action.
See an example in [Minotaor's](https://github.com/Edinburgh-Genome-Foundry/Minotaor) `/.github/workflows/document.yml` file.

**Push to GitHub & manually trigger the workflow**

Check that the documentation looks correct before creating a release.


---

#### References

Sphinx documentation: https://www.sphinx-doc.org/en/master/usage/installation.html

Sphinx tutorial: https://sphinx-rtd-tutorial.readthedocs.io/

Numpydoc format: https://numpydoc.readthedocs.io/en/latest/format.html

Example numpydoc: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


---

## Previous approach (pre-2025): Generating the HTML docs

This explains how to use sphinx to autodocument a Python library, and how to
host it on Github. This is WAY over-complicated, but hey, it may get simpler one day
*[note from future: it did get simpler].*

Your project should have the following structure, where ``docs`` is the folder
attached in this repo:

```
project_projectname            <= all-encompassing folder
+-- ProjectName                <= root of the git repo
    +-- projectname            
    |   +-- source_file1.py
    |   +-- source_file2.py
    +-- docs                   <= copied from THIS repo.
    |   +-- ...
    +-- README.md
    +-- setup.py
    +-- etc.
```


Personalize the ``docs`` folder:

- Use your editor to automatically change all mentions of "Primavera" in the
  docs folder to your project's name.
- Change the content of ``docs/index.rst`` (that's the homepage of the docs)
- Look around for more options and learn how to use sphinx to change more stuff.

To build the docs, first install the dependencies:

```
sudo pip install sphinx sphinx_rtd_theme sphinx-press-theme numpydoc sphinxcontrib-mermaid recommonmark
```

Then each time you want to re-generate the docs and display them in a Firefox,
run the ``makehtml.sh`` at the root of the ``docs`` folder, by typing
``makehtml.sh`` in a terminal.

## Hosting the docs on Github

If your repo already has a ``gh-pages`` branch, go to section 'Package with a `gh-pages` branch' below.

### Package does not have `gh-pages` branch

First make sure that your Python library is on Github and can be cloned using
```
git clone git@github.com:myusername/mylibrary
```

Now notice that the generation of the HTML docs has created files in a new folder called ``html`` located here:

```
project_projectname            <= all-encompassing folder
+-- built_docs
    +-- html                   <== this folder !
        +-- ...
+-- ProjectName                <= root of the git repo
    +-- ...
```

Go to the ``html`` folder, remove all the files in it, and pull your github project in this folder:

```
git clone git@github.com:myusername/mylibrary .
```

Mind the ``.`` at the end. Run the following commands, still in the ``html`` folder:

```
git branch gh-pages
git symbolic-ref HEAD refs/heads/gh-pages  # auto-switches branches to gh-pages
rm .git/index
git clean -fdx
touch .nojekyll
```

The final line adds a ``.nojekyll`` file in the ``html`` folder.

Congratulations, you have a gh-pages branch in your project.


### Package with a `gh-pages` branch

From pkgname/docs/ run:

	./makehtml.sh

This will create `built_docs/` one level above the pkgname directory. Go to `built_docs/` and delete `html/`. Clone the gh-pages branch into `html`:

    git clone --single-branch --branch gh-pages git@github.com:Edinburgh-Genome-Foundry/Primavera.git html


### Let's push to Github:

Now from your ``docs`` folder, run once more ``makehtml`` to regenerate the docs.

Come back to the ``html`` folder and push it to github:

```
git add .
git commit
git push origin gh-pages
```

Yeah ! You're done. Your docs are now hosted there (replace Primavera with your
Github repo's name):

[https://edinburgh-genome-foundry.github.io/Primavera/](https://edinburgh-genome-foundry.github.io/Primavera/)

Repeat this *Let's push to Github* procedure everytime you want to
update the docs.
