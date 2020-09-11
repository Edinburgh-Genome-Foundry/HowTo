# Create HTML docs hosted on Github for your Python project

This explains how to use sphinx to autodocument a Python library, and how to
host it on Github. This is WAY over-complicated, but hey, it may get simpler one day.

## Generating the HTML docs

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
