*** Settings ***

Documentation  Customer Use Cases
Library  Selenium2Library


*** Test Cases ***

Customer Can Search for a Restaurant With Designated Criteria
    Input Text  xpath=//*[@id='search-form']//*[@id='restaurant-property-input']  Metro Manila
	Select From List  xpath=//*[@id='search-form']//*[@id='party-size-input']  2
	Click Element  xpath=//*[@id='search-form']//*[@class='ui-datepicker-trigger']
	Click Element  xpath=//*[contains(@class, 'ui-datepicker-today')]
	Click Element  xpath=//*[@id='search-form']//*[@id='time-input']
	Click Element  xpath=//*[@class='ui-timepicker-list']/li[1]
	Click Button  xpath=//*[@id='search-form']//*[@id='submit-button']
