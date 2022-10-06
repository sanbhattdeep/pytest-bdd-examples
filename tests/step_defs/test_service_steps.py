from pytest_bdd import given, when, then, scenarios, parsers

import requests

# Shared variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com'

# Scenarios

scenarios('..//features/service.feature')


# Given steps

@given('the DuckDuckGo API is queried with "<phrase>"', converters={"phrase": str}, target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


# Then steps


@then('the response contains results for "<phrase>"', converters={"phrase": str})
def ddg_response_contains(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'), converters={"phrase": str})
def ddg_response_code(ddg_response, code):
    assert code == ddg_response.status_code

