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
