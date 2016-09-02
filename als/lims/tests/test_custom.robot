*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=.5
Resource  keywords.txt
Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Test Cases ***


*** Keywords ***

Start browser
    Open browser         http://localhost:55001/plone/
    Set selenium speed   0.2
