# Testing Jupyter Notebooks with pytest

## Installation

`python3 -m pip install -r requirements.txt`

## Execution

Navigate to the directory of `test_notebook.py` and run `pytest --tb=no` from the command-line.

The option `--tb=no` hides the traceback from the notebook.

The option `-v` and `-vv` increase the verbosity of pytest.



## Tests

The script `test_notebooks.ipynb` defines a runner for all notebooks in the same directory.

All cells in these notebooks are executed.

The test (should) fail, if any cells fail to execute.

`add_numbers.ipynb`  
Defines a function within a cell and executes this function in another cell.  
This notebook should `PASS`.

`folded_code_cells.ipynb`  
Defines a function and global objects witih folded cells (`exercise2`) and executes the function with the defined global objects in another cell.  
This notebook should `PASS`.

`missing_imports.ipynb`  
Defines a function wich requires not yet imported modules.  
This notebook should `FAIL`.


