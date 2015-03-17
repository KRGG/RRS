*** Settings ***

Documentation  Blackbox tests for the generic template
Library  Selenium2Library
Suite setup  Open Browser  http://localhost:8000  browser=googlechrome
Suite teardown  Close Browser


*** Test Cases ***

Check if all required links are present
    Element should be visible  about-link
    Element should be visible  terms-link
    Element should be visible  privacy-statement-link
    Element should be visible  sitemap-link