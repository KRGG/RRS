*** Settings ***

Documentation  Verifies presence of required components per page
Library  Selenium2Library
Suite setup  Open Browser  http://localhost:8000/  browser=googlechrome
Suite teardown  Close Browser


*** Test Cases ***

Check if generic template links are present
	Page Should Contain Link  xpath=//*[@id='header']//*[@id='about-link']
	Page Should Contain Link  xpath=//*[@id='footer']//*[@id='terms-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='privacy-policy-link']
    Page Should Contain Link  xpath=//*[@id='footer']//*[@id='sitemap-link']
    
Check that location of bottom overflow content is above footer
	Go to  http://localhost:8000/test-dedicated/overflow
	Scroll '#content-base' to '#bottom-of-content'
	${footer_y_location}=  Get Vertical Position  xpath=//*[@id='footer']
	${content_bottom_y_location}=  Get Vertical Position  xpath=//*[@id='bottom-of-content']
	Should Be True  ${footer_y_location} > ${content_bottom_y_location}
    
Check if view restaurant page elements are present
	Go to  http://localhost:8000/restaurant/1
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
	