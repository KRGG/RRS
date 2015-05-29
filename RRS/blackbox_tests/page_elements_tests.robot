*** Settings ***

Documentation  Verifies presence of required components per page
Library  Selenium2Library
Library  robot_libraries.DjangoLibrary
Suite setup  Open Browser  http://localhost:8000/  browser=googlechrome
Suite teardown  Close Browser


*** Test Cases ***

Check if generic template links are present
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='about-link']
	Page Should Contain Link  xpath=//*[@id='footer']//*[@id='terms-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='privacy-policy-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='sitemap-link']
    Check That 'login' Is Accessible From xpath=//*[@id='header']//*[@id='log-in-link']
    Check That 'signup' Is Accessible From xpath=//*[@id='header']//*[@id='sign-up-link']
    Check That 'index' Is Accessible From xpath=//*[@id='header']//*[@class='navbar-brand']
    
    
Check if view restaurant page elements are present
	Go to  http://localhost:8000/restaurant/1/
	Check That 'index' Is Accessible From xpath=//*[@id='header']//*[@class='navbar-brand']
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
Scroll ${scrollable} to ${element}
	Execute Javascript  $(${scrollable}).scrollTop($(${element}).position().top);
	
Check That '${named_url}' Is Accessible From ${locator}
	${url}=  Get Element Attribute  ${locator}@href
	${resolved_name}=  Resolve Url  ${url}
    Should Be Equal  ${resolved_name}  ${named_url}
	