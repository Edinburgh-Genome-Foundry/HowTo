"""Here we will pretend that we are testing the library numpy."""

import os # useful for generating file paths
import numpy
import matplotlib
matplotlib.use('Agg') # necessary if you are using matplotlib in Travis tests.


def test_arrays():
    array = numpy.array([1, 2, 3])
    assert array.sum() == 6


# Every time you will neeed to write down files, provide the ``tmpdir``
# parameter to your test to create a temporary directory to write to:
def test_with_file_writing(tmpdir):
    with open(os.path.join(str(tmpdir), "mytestfile.txt"), "w+") as f:
        for i in numpy.linspace(0, 10, 100):
            f.write(i)
