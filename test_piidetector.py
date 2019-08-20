import pytest
import re

#https://stackoverflow.com/questions/4087468/ssn-regex-for-123-45-6789-or-xxx-xx-xxxx
SSN_PATTERN = "^\d{3}[ -]?\d{2}[ -]?\d{4}$"

@pytest.mark.parametrize("ssn_num, expected",
[
  ("555-22-3232",True),
  ("55-22-3333", False),
  ("555223333", True),
  ("555 22 2323", True)
])
def test_ssn(ssn_num, expected):
    assert bool(re.search(SSN_PATTERN,ssn_num)) == expected


#https://daxondata.com/javascript-php-and-regular-expressions-for-international-and-us-phone-number-formats
PHONE_NUMBER_PATTERN = "\d?(\s?|-?|\+?|\.?)((\(\d{1,4}\))|(\d{1,3})|\s?)(\s?|-?|\.?)((\(\d{1,3}\))|(\d{1,3})|\s?)(\s?|-?|\.?)((\(\d{1,3}\))|(\d{1,3})|\s?)(\s?|-?|\.?)\d{3}(-|\.|\s)\d{4}"

@pytest.mark.parametrize("phone_num, expected",
[
  ("123-456-7890",True),
  ("(123) 456-7890", True),
  ("123 456 7890", True),
  ("123.456.7890", True),
  ("+91 (123) 456-7890", True),
  ("+555 5555 5555", True),
  ("+1 777 777 7777", True),
  ("+51 777 777777-0", True),
  ("+51 (0)777 777777", True),
  ("+77 77777 77777", True),
  ("777 555-5555", True)
])
def test_phone(phone_num, expected):
    assert bool(re.search(PHONE_NUMBER_PATTERN,phone_num)) == expected

#https://emailregex.com/
EMAIL_PATTERN = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
@pytest.mark.parametrize("email_address, expected",
[
  ("test@test.com", True),
  ("a.little.unusual@example.com", True),
  ("a.little.more.unusual@dept.example.com", True)
])
def test_email(email_address, expected):
    assert bool(re.search(EMAIL_PATTERN, email_address)) == expected

#http://www.richardsramblings.com/regex/credit-card-numbers/
CREDIT_CARD_PATTERN = "^(?:3[47]\d{2}([\s\-]?)\d{6}([\s\-]?)\d|(?:(?:4\d|5[1-5]|65)\d{2}|6011)([\s\-]?)\d{4}([\s\-]?)\d{4}([\s\-]?))\d{4}$"

@pytest.mark.parametrize("credit_card, expected",
[
  ("371449635398431", True), # American Express
  ("6011000990139424", True), # Discover
  ("4532509954095153", True), # Visa
  ("3714-496353-98431", True), # American Express
  ("4012-8888-8888-1881", True), # Visa
])
def test_credit_card(credit_card, expected):
    assert bool(re.search(CREDIT_CARD_PATTERN, credit_card)) == expected

#https://gist.github.com/cgudea/7c558138cb48b36e785b
DMS_LATITUDE_PATTERN = "-?((90\/[0]{0,}\/[0]{0,}$)|([1-8]?\d))(\/|\:|\ )(([1-5]?\d))(\/|\:|\ )[1-5]?\d(\.\d{0,})"

@pytest.mark.parametrize("lattitude, expected",
[
  ( '-12/23/59.999999999999999', True),
  ( '-1/2/1.000234', True),
  ( '-1:2:12.000234', True), 
	( '0 59 0.22', True),
  ( '60/34/34', True),
  ( '20/60/0', False),
  ( '80/60/1.11', False), 
  ( '80/59/70', False),
  ( '90/59/0', False),
  ( '86/60/1', False)
])
def test_dms_latitude_pattern(latitude, expected):
    assert bool(re.search(DMS_LATITUDE_PATTERN, expected)) == expected

#https://gist.github.com/cgudea/7c558138cb48b36e785b
DMS_LONGTITUDE_PATTERN =  "-?((90\/[0]{0,}\/[0]{0,}$)|([1-8]?\d))(\/|\:|\ )(([1-5]?\d))(\/|\:|\ )[1-5]?\d(\.\d{0,})"
@pytest.mark.parametrize("latitude, expected",
[('123:60:59.99999999', False),
 ('-180:12:0', False),
 ('180:60:0', False),
 ('700 50 50.11', False),
 ('23/79/22.22', False), 
 ('0 60 2.2', False),
 ('0 60 0', False),
 ('-179/59/0.23', True),
 ('127/12/12.223', True),
 ('-180/0/0', True),
 ('179:59:59.99999999', True),
 ('-59:13:58.22212345', True),
 ('0:0:2.3', True),
 ('127 12 12.333', True),
 ('180 0 0', True),
 ('-0 0 0.00001', True)
 ])
def test_dms_longtitude_pattern(longtitude, expected):
    assert bool(re.search(DMS_LONGTITUDE_PATTERN, expected)) == expected

    