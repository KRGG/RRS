*** Settings ***
Resource  ./user_dependent_variables.robot

*** Keywords ***
Setup Test Environment
	Open Browser  http://localhost:8000/  browser=${USER_DEPENDENT_BROWSER}
	
Teardown Test Environment
	Close Browser