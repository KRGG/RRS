*** Settings ***
Library  robot_libraries.DjangoLibrary

*** Variables ***
${DOMAIN}  http://localhost:8000

*** Keywords ***
Build From Named URL  
    [Arguments]  ${url_name}  @{url_params}
    [Return]  ${full_url}
    ${path}=  Reverse Url  ${url_name}  @{url_params}
    ${full_url}=  Catenate  SEPARATOR=  ${DOMAIN}  ${path}