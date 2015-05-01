*** Settings ***

Documentation  Verifies presence of required components per page
Library  HttpLibrary.HTTP
Library  Selenium2Library


*** Test Cases ***

Check if generic template links are present
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='about-link']
	Page Should Contain Link  xpath=//*[@id='footer']//*[@id='terms-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='privacy-policy-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='sitemap-link']
    Link Should Be Accessible  xpath=//*[@id='header']//*[@id='log-in-link']
    Link Should Be Accessible  xpath=//*[@id='header']//*[@id='sign-up-link']
    
Check if view restaurant page elements are present
	Go to  http://localhost:8000/restaurant/1/
	Page Should Contain Element  xpath=//*[@id='banner-img']
	Page Should Contain Element  xpath=//*[@id='restaurant-name']
	Page Should Contain Element  xpath=//*[@id='restaurant-location']
	Page Should Contain Element  xpath=//*[@id='cuisine-type']
	Page Should Contain Element  xpath=//*[@id='price-range']
	
	Page Should Contain Element  xpath=//*[@id='reservation-form']//*[@id='people-input']
	Page Should Contain Element  xpath=//*[@id='reservation-form']//*[@id='date-input']
	Page Should Contain Element  xpath=//*[@id='reservation-form']//*[@id='time-input']
	Page Should Contain Element  xpath=//*[@id='reservation-form']//*[@id='submit-button']
	
*** Keywords ***
Link Should Be Accessible
	[Arguments]  ${locator}
	${url}=  Get Element Attribute  ${locator}@href
    GET  ${url}
Scroll ${scrollable} to ${element}
	Execute Javascript  $(${scrollable}).scrollTop($(${element}).position().top);
	