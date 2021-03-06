import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open('projectname/version.py').read()) # loads __version__

setup(name='projectname',
      version=__version__,
      author='Author',
    description='Read/write microplate and picklist data for lab automation',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords="microplate biology parser converter report",
    packages= find_packages(exclude='docs'),
    install_requires= ['pandas', 'xlwt', 'xlrd', 'python-box', 'numpy',
                       'matplotlib', 'tqdm'])
