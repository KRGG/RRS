*** Settings ***
Library  Selenium2Library
Library  robot_libraries.DjangoLibrary
Resource  resources/user_dependent_variables.robot
Resource  resources/keywords.robot
Suite setup  Setup Test Environment
Suite teardown  Teardown Test Environment

*** Keywords ***
Setup Test Environment
	${starting_url}=  Build From Named URL  index
	Open Browser  ${starting_url}  browser=${USER_DEPENDENT_BROWSER}
	
Teardown Test Environment
	Close Browser