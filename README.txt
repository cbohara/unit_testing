Notes from Unit Testing with Python from Pluralsight

################
test case design
################

test case name
should give good indication of what functionality is or is not working

################
unittest
################

@unittest.skip("message")
decorator put on top of the method you want to skip for now

test fixture
before each test method is run, the test runner will run setUp()
