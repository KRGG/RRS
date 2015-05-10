*** Settings ***

Documentation  Customer Use Cases
Library  Selenium2Library


*** Test Cases ***

Customer Can Search for a Restaurant With Designated Criteria
	Select From List  xpath=//*[@id='search-form']//*[@id='party-size-input']  2
	Click Element  xpath=//*[@id='search-form']//*[@id='date-input']
	Click Element  xpath=//*[contains(@class, 'ui-datepicker-today')]
	Click Element  xpath=//*[@id='search-form']//*[@id='time-input']
	Click Element  xpath=//*[@class='ui-timepicker-list']/li[1]
