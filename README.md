# bink_test

## How to use:
- Run the main script and provide the path to your dataset, for example: `python main.py dataset.csv`
- You will be met with an option menu, select one of the options and follow the instructions.

## How to run tests:
- there are two test files in the `test` directory.
- You can run `python test/test_data_processor.py` and `python test/test_helpers.py`

## Notes:
- I tried to keep it simple and not use any external libraries 
- I assumed that the structure of the `.csv` dataset (e.g. the column names) is constant. Otherwise, I would add more error handling, for example for `KeyError`
- I did not test the printing functions in the `DataProcessor` class. Where relevant, I moved logic into the helpers module and wrote unit tests for those. With a more thorough error handling, I'd add more tests with bad inputs.