Notes from Unit Testing with Python from Pluralsight
https://app.pluralsight.com/library/courses/unit-testing-python/

################
unittest
################

python -m unittest

@unittest.skip("message")
decorator put on top of the method you want to skip for now

test fixture
before each test method is run, the test runner will run setUp()

#############
pytest
#############

python -m pytest

test needs to start with test_

pytest.skip("message")
put within the test function

use the @pytest.fixture to generate a resource that will be passed to the function during runtime
@pytest.fixture
def phonebook(tmpdir):
    # tmpdir is a built in pytest resource so files don't have to be written locally
    return Phonebook(tmpdir)

python -m pytest --fixtures
shows built-in and fixtures we have built

-------------------------------------------------------------------------
Notes from TutorialsPoint
https://www.tutorialspoint.com/unittest_framework/unittest_framework_quick_guide.htm

test fixture
prep needed to perform a task and any associated cleanup actions
ex: creating a temp directory and then removing the temp directory

test case
smallest unit of testing
checks for specific response to a particular set of inputs

test suite
collection of test cases, test suites, or both
aggegrates tests that should be run together

test runner
orchestrates the execution of tests
provides outcome to the user

