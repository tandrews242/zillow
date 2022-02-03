# Zillow Mortgage Calculator
https://www.zillow.com/mortgage-calculator/

This repo contains automated tests for the interest rate field in Zillow's mortgage calculator. Please follow the instructions below to run the tests.

## Instructions
1. Clone this repo to your Github folder
2. Using a terminal, navigate to the project directory `../github/zillow`
3. Create and activate a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for Python 3
4. Install pytest `pip install pytest`
5. Install selenium `pip install selenium`
6. Intall the webdriver manager `pip install webdriver-manager`
7. Navigate to the tests folder `cd tests`
8. Execute the tests by using the command `pytest <file>` (i.e. `pytest test.py`)

## Testing Notes
1. Without having access to the source that determines what the default interest rates are, I cannot validate that the interest rates generated are accurate. I can only validate that the interest rate changes to something other than the default value when new information (i.e. Loan term, House price) is entered in the form.
2. As these tests continue to scale, it would be helpful to have a library of functions that could be reused across different files and tests. For example, I would create a function specifically for entering a new interest rate. I would then call this function whenever a new interest rate needs to be entered. This would prevent code duplication and would make the test suite easier to maintain.
3. As more tests are written, it would be important to organize them into different test suites. It would be important to make sure that each test runs efficiently to minimize the time it takes to run each suite. Suites could be run in parallel to reduce total run time.
4. The results for these tests should logged and recorded in a CI / test management environment. The test should record relevant information such as the build number, timestamp, and environment. It is important to keep a detailed audit trail of past test results.
5. I would improve the logging for each step so that it is clear what is being executed at each step. This would make it easier to debug tests when a step fails.
