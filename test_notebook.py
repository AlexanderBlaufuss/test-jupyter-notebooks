import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

import os

notebooks = [nb for nb in os.listdir() if nb.endswith('.ipynb')]

@pytest.mark.parametrize("notebook", notebooks)
def test_nb(notebook):
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=100, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})

    except CellExecutionError:
        print('Error')
        raise


