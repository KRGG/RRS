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
  Click Element  xpath=//*[@id='search-form']//*[@id='party-size-input-trigger']
  Click Element  xpath=//*[@id='party-size-input-list']/li[1]
  
Select Date
  Click Element  xpath=//*[@id='search-form']//*[@class='ui-datepicker-trigger']
  Click Element  xpath=//*[contains(@class, 'ui-datepicker-today')]
  
Select Time
  Click Element  xpath=//*[@id='search-form']//*[@id='time-input-trigger']
  Click Element  xpath=//*[@class='ui-timepicker-list']/li[1]
	