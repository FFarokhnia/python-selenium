import pytest, requests, csv
from assertpy.assertpy import assert_that
from pathlib import Path
import os

# Exercise 2.1
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse
test_data_zip = [
    ('us', '90210', 'Beverly Hills'),
    ('it', '50123', 'Firenze'),
    ('ca', 'Y1A', 'Whitehorse')
]


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
# and checks that the values for the 'place name' elements correspond
# to those that are specified in the test data object
@pytest.mark.parametrize('country_code, zip_code, place', test_data_zip)
def test_place_name_param(country_code, zip_code, place):
    response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
    places = response.json()['places']
    # place_names = places['place name']
    assert_that(places).extracting('place name').contains(place)


# Exercise 2.3
# Create the same test data as above, but now in a .csv file, for example:
# us,90210,Beverly Hills
# it,50123,Firenze
# ca,Y1A,Whitehorse
# Place this .csv file in the answers folder of the project
@pytest.fixture()
def create_write_place_name_csv_file():
    file_path = Path.cwd().joinpath('answers')
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # write_file(file_path,test_data_zip)
    write_csv_file(file_path, test_data_zip)


def write_file(file_path, data):
    f = open(file_path.joinpath('test_data.csv'), 'w')
    for el in data:
        f.write(str(el))
        f.write('\n')


def write_csv_file(file_path, data):
    csv_file = open(file_path.joinpath('test_data.csv'), mode='w', newline='')
    writer = csv.writer(csv_file, delimiter=' ')
    writer.writerows(data)


# Exercise 2.4
# Create a method read_data_from_csv() that reads the file from 2.3 line by line
# and creates and returns a test data object from the data in the .csv file
def read_file(expected_path):
    file_path = Path.cwd().joinpath(expected_path)
    with open(file_path) as f:
        test_data = f.read()
    return test_data


def read_csv_file(expected_path):
    test_data = []
    file_path = Path.cwd().joinpath(expected_path)
    with open(file_path, newline='') as csv_f:
        reader = csv.reader(csv_f, delimiter=' ')
        test_data.append(reader)
    return test_data


# Exercise 2.5
# Change the data driven test from Exercise 2.2 so that it uses the test data
# from the .csv file instead of the test data that was hard coded in this file
def test_place_param_csv(create_write_place_name_csv_file):
    @pytest.mark.parametrize('country_code, zip_code, place', read_csv_file('answers/test_data.csv'))
    def test_place_name(country_code, zip_code, place):
        response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
        places = response.json()['places']
        # place_names = places['place name']
        assert_that(places).extracting('place name').contains(place)
