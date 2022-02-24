# Contributing to an EGF project

We welcome bug reports, feature requests, and pull requests.

## Development

Development happens on feature branches, which are merged to the `dev` branch. Before each release, version number is updated, then `dev` is merged into the `master` (or `main`) and uploaded to PyPI. This ensures there is only one codebase for each version number.

EGF Python packages conform to Black and Flake8 requirements, which are preferably enforced using pre-commit hooks.

### Versioning

The semantic versioning scheme is used (<https://semver.org>). Python package version numbers are single-sourced, see [this repo as an example](https://github.com/Edinburgh-Genome-Foundry/Minotaor/blob/main/setup.py#L4).

### Testing

Tests are included for each functionality.

[Travis CI](https://travis-ci.org/github/Global-Biofoundries-Alliance/SynBioPython) or GitHub Actions is used for continuous integration.

### Documentation

A docstring is included for each user function. We use [Portray](https://github.com/timothycrosley/portray/) or Sphinx for documentation.

#### Portray

See [this function](https://github.com/Edinburgh-Genome-Foundry/Minotaor/blob/main/minotaor/minotaor.py#L53) for an example on formatting.

To generate the documentation, run this from the Python package repo dir:

```bash
portray as_html -m pkgname -o docs --overwrite
```

Then commit with git.

#### Sphinx

See details at [Create HTML docs](https://github.com/Edinburgh-Genome-Foundry/HowTo/tree/master/python/create_github_html_docs).

## Pull requests

Please follow the below guidelines:

* For new features, first file an issue for discussion.
* Fork the repo.
* Ensure that the new code conforms to the development guidelines, including documentation and passing tests.
* Make sure that you have the legal right to contribute the code under the project's licence.
* Make a PR to the `dev` branch of the EGF repo.

See [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow) for more details.
