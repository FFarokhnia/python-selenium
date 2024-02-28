import requests , json
from assertpy.assertpy import assert_that
# import pytest
from conftest import BASE_URL



# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
def test_status_code():
    response = requests.get(url=BASE_URL)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_resp_content_type():
    response = requests.get(url=BASE_URL)
    resp_content_type = response.headers['Content-Type']
    assert_that(resp_content_type).is_equal_to('application/json')

# Exercise 1.3
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'country' has a value equal to 'United States'
def test_resp_body():
    response = requests.get(url=BASE_URL)
    resp_body_country = response.json()['country']
    assert_that(resp_body_country).is_equal_to('United States')
    # assert_that(resp_body_country).is_equal_to('Germany')

# Exercise 1.4
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places
# has a value equal to 'Beverly Hills'
def test_place_name():
    response = requests.get(url=BASE_URL)
    resp_body_first_place = response.json()['places'][0]
    resp_body_first_place_name = resp_body_first_place['place name']
    assert_that(resp_body_first_place_name).is_equal_to('Beverly Hills')
    # assert_that(resp_body_first_place_name).is_equal_to('Dresden Friedrichstadt')

# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)
def test_place_is_not_empty():
    response = requests.get(url=BASE_URL)
    resp_body_places = response.json()['places']
    # resp_body_first_place_name = resp_body_place['place name']
    assert_that(len(resp_body_places)).is_equal_to(1)

    #changes happened for github
    #second change is done for github
    #third change is done for github but it is not tracked
    #forth change is done
def mahsatest():
    return false
    
