from lxml import etree
import requests
from assertpy.assertpy import assert_that


# Exercise 5.1
# Write a test that does the following:
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Check that the root element name is 'account'
# Check that the root element has no attributes
# Check that the root element has no text
def test_get_xml():
    url = 'https://parabank.parasoft.com/parabank/services/bank/accounts/12345'
    response = requests.get(url=url)
    response_body_as_xml = etree.fromstring(response.content)
    xml_tree = etree.ElementTree(response_body_as_xml)
    root = xml_tree.getroot()
    assert_that(root.tag).is_equal_to('account')
    assert_that(root.attrib).is_none()
    assert_that(root.text).is_none()


# Exercise 5.2
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Find the customerId element in the tree
# Check that the text of the customerId element is '12212'
def test_get_xml_element_tree():
    url = 'http://parabank.parasoft.com/parabank/services/bank/accounts/12345'
    response = requests.get(url=url)
    response_body_as_xml = etree.fromstring(response.content)
    xml_tree = etree.ElementTree(response_body_as_xml)
    customer_id = xml_tree.find('customerId')
    assert_that(customer_id.text).is_equal_to('12212')


# Exercise 5.3
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts
# Parse the response into an XML ElementTree
# Find all 'account' elements in the entire XML document
# Check that there are more than 5 of these 'account' elements
def test_check_number_of_accounts_for_12212_greater_than_five():
    url = 'http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts'
    response = requests.get(url=url)
    xml_response_body = etree.fromstring(response.content)
    xml_tree = etree.ElementTree(xml_response_body)
    accounts = xml_tree.findall('.//account')
    assert_that(len(accounts)).is_greater_than(5)


# Exercise 5.4
# Repeat Exercise 5.3, but now check that:
# - at least one of the accounts is of type 'SAVINGS' (Google!)
# - there is no account that has a customerId that is not equal to 12212
#   (Use your creativity with the last one here... There is a solution, but I couldn't
#    find it on Google.)
def test_use_xpath_for_more_sophisticated_checks():
    url = 'http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts'
    response = requests.get(url=url)
    xml_response_body = etree.fromstring(response.content)
    xml_tree = etree.ElementTree(xml_response_body)
    savings_accounts = xml_tree.findall('.//account/type/[.="SAVINGS"]')
    assert_that(len(savings_accounts)).is_greater_than(0)
    accounts_with_incorrect_customer_id = xml_tree.findall('.//account/customerId[!.="12212"]')
    assert_that(len(accounts_with_incorrect_customer_id)).is_equal_to(0)
