*** Settings ***
<<<<<<< HEAD
Library  robot_libraries.DjangoLibrary

*** Variables ***
${DOMAIN}  http://localhost:8000

*** Keywords ***
Build From Named URL  
    [Arguments]  ${url_name}  @{url_params}
    [Return]  ${full_url}
    ${path}=  Reverse Url  ${url_name}  @{url_params}
    ${full_url}=  Catenate  SEPARATOR=  ${DOMAIN}  ${path}
=======
Resource  ./user_dependent_variables.robot

*** Keywords ***
Setup Test Environment
	Open Browser  http://localhost:8000/  browser=${USER_DEPENDENT_BROWSER}
	
Teardown Test Environment
	Close Browser
>>>>>>> Organized blackbox tests
