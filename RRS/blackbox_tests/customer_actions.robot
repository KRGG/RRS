*** Settings ***

Documentation  Customer Use Cases
Library  Selenium2Library


*** Test Cases ***

Customer Can Search for a Restaurant With Designated Criteria
  Input Text  xpath=//*[@id='search-form']//*[@id='restaurant-property-input']  Metro Manila
  Enter Party Size
  Select Date
  Select Time
  Click Button  xpath=//*[@id='search-form']//*[@id='submit-button']

*** Keywords ***
Enter Party Size
  Input Text  xpath=//*[@id='search-form']//*[@id='party-size-input']  2
  
Select Date
  Click Element  xpath=//*[@id='search-form']//*[contains(@class, 'ui-datepicker-trigger')]
  Click Element  xpath=//*[contains(@class, 'ui-datepicker-today')]
  
Select Time
  Click Element  xpath=//*[@id='search-form']//*[@id='time-input']
  Click Element  xpath=//*[@class='ui-timepicker-list']/li[1]
	