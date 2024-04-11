*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Open Google.com Test
    Open Browser    https://www.google.com    Chrome
    Maximize Browser Window
    [Teardown]    Close Browser
