*** Settings ***

Documentation  Blackbox tests for the generic template
Library  Selenium2Library
Suite setup  Open Browser  http://localhost:8000  browser=googlechrome
Suite teardown  Close Browser


*** Test Cases ***

Check if required header links are present
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='mobile-link']
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='sign-up-link']
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='log-in-link']
