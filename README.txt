Notes from Unit Testing with Python from Pluralsight

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

