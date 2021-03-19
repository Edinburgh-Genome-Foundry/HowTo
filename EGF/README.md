<p align="center">
<img alt="EGF logo" title="EGF" src="egf.png" width="120">
</p>

# How to install and use EGF packages


## Install

EGF packages were developed on Python v3.6 in Ubuntu (18.04), and in most cases work well in other Python versions and operating systems.


### Option 1: Anaconda

It's recommended to use a separate Python installation with its own environment, and not the operating system's Python. Install the [Anaconda](https://www.anaconda.com) package manager and create an environment:
```
conda create --name egf python=3.6
```
Activate:
```
conda activate egf
```
The environment name `(egf)` should appear before the terminal prompt. EGF packages are not packaged for conda, but can be installed with `pip install packagename`.

[JupyterLab](https://jupyterlab.readthedocs.io) provides a web-based user-friendly interface for running Python code.


### Option 2: Docker

Some packages or their dependencies may not work properly on other operating systems. In this case, you can use [Docker](https://www.docker.com); and build your own image by installing the EGF packages on an Ubuntu 18.04 / Python v3.6 base image.


---


## Use

A web interface for many packages is provided at the [EGF's Collection of Useful Biological Apps (CUBA)](https://cuba.genomefoundry.org/).

More customized use requires knowledge of Python, and, for certain packages, other programming and markup languages: HTML, CSS, JavaScript, SQL.


## Change and improve

Almost all EGF packages are [free software](https://www.gnu.org/philosophy/free-sw.en.html), released under the MIT license. Feel free to change and improve the code. If you would like to contribute, then please file an issue for discussion.
