import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# Scenarios

scenarios('../features/web.feature')


# When steps


@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)


# Then steps


@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements(By.XPATH, xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element(By.ID, 'links')
    assert len(links_div.find_elements(By.XPATH, '//div')) > 0
    # Check search phrase
    search_input = browser.find_element(By.NAME, 'q')
    assert not search_input.get_attribute('value') == phrase
