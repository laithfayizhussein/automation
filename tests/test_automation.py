from automation import __version__


def test_version():
    assert __version__ == '0.1.0'


from automation.automation import email , telephone
import pytest
test = ' this the my first time that i write test will fillter the emails and phone number like hh@gmail.com and laith@gmail.com! 548-456-7673 and 23-3434-3434 and 222-444-5553 and 344-234-2332'

def test_phone_numbers():
    # i will looking for how i can test the string 
    actual = telephone(test)
    expected =('548-456-7673','344-234-2332','222-444-5553','23-3434-3434')
    assert actual == expected

def test_emails():
    actual = email(test)
    expected =('laith@gmail.com', 'hh@gmail.com')
    assert actual == expected