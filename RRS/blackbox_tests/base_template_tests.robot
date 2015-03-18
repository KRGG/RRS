*** Settings ***

Documentation  Blackbox tests for the generic template
Library  Selenium2Library
Suite setup  Open Browser  http://localhost:8000  browser=googlechrome
Suite teardown  Close Browser


*** Test Cases ***

Check if required header links are present
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='about-link']

Check if required footer links are present
	Page Should Contain Link  xpath=//*[@id='footer']//*[@id='terms-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='privacy-policy-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='sitemap-link']