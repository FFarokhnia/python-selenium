from lxml import etree
from assertpy.assertpy import assert_that
import requests


# Exercise 4.1
# Create a function create_xml_body_from_string()
# that returns a docstring (with triple double quotes)
# containing the following XML document:
# <payee>
#     <name>John Smith</name>
#     <address>
#         <street>My street</street>
#         <city>My city</city>
#         <state>My state</state>
#         <zipCode>90210</zipCode>
#     </address>
#     <phoneNumber>0123456789</phoneNumber>
#     <accountNumber>12345</accountNumber>
# </payee>
def create_xml_body_from_string():
    return """
           <payee>
                <name>John Smith</name>
                <address>
                    <street>My street</street>
                    <city>My city</city>
                    <state>My state</state>
                    <zipCode>90210</zipCode>
                </address>
                <phoneNumber>0123456789</phoneNumber>
                <accountNumber>12345</accountNumber>
            </payee> 
            """


# Exercise 4.2
# Write a test that POSTs the object created in 4.1
# to https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500
# Set the request header 'Content-Type' to 'application/xml'
# Then check that the response status code is 200
# and that the value of the response header 'Content-Type' is also equal to 'application/xml'
def test_post_xml_string():
    url = 'https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500'
    headers = {
        "Content-Type": "application/xml"
    }

    response = requests.post(url=url, data=create_xml_body_from_string(), headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.request.headers['Content-Type']).is_equal_to('application/xml')


# Exercise 4.3
# Write a method create_xml_body_using_elementtree() that returns
# the same request body as in Exercise 4.1, but now uses the
# ElementTree library (I've imported that for you already, it's available as 'et')
# Make your life a little easier by specifying all element values as strings
def create_xml_body_using_elementtree():
    payee = etree.Element("payee")
    name = etree.SubElement(payee, 'name')
    name.text = 'John Smith'
    address = etree.SubElement(payee, 'address')
    street = etree.SubElement(address, 'street')
    street.text = 'My street'
    city = etree.SubElement(address, 'city')
    city.text = 'My city'
    state = etree.SubElement(address, 'state')
    state.text = 'My state'
    zip_code = etree.SubElement(address, 'zipcode')
    zip_code.text = '90210'
    phone_number = etree.SubElement(payee, 'phoneNumber')
    phone_number.text = '0123456789'
    account_number = etree.SubElement(payee, 'accountNumber')
    account_number.text = '12345'
    return payee

# Exercise 4.4
# Repeat Exercise 4.2, but now use the XML document created in Exercise 4.3
# Don't forget to convert the XML document to a string before sending it!
def test_post_xml():
    url = 'https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500'
    headers = {
        "Content-Type": "application/xml"
    }

    response = requests.post(url=url, data=etree.tostring(create_xml_body_using_elementtree()), headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.request.headers['Content-Type']).is_equal_to('application/xml')
