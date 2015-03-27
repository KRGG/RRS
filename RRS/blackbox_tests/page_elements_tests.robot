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
    
Check that long-content scrolls down
	Element Should Not Be Visible  xpath=//*[@id='test']
	${hi}=  Get Vertical Position  xpath=//*[@id='footer']
	Log To Console  ${hi}
	${hi}=  Get Vertical Position  xpath=//*[@id='test']
	Log To Console  ${hi}
    
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
	
	