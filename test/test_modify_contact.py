# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_user(Contact(firstname="test_firstname1", bday="1", aday="2", amonth="January", bmonth="February"))
    app.contact.modify_first(
        Contact(title="test_title1", company="test_company1", address="test_address1", home="test_home1",
                mobile="test_mobile1", work="test_work1", fax="test_fax1", email="test_email_1", email2="test_email2_2",
                email3="test_email3_3", homepage="test_homepage1", firstname="test_firstname1",
                middlename="test_middlename1", lastname="test_lastname1", nickname="test_nickname1",
                notes="test_notes1", phone2="test_phone3", address2="test_address3", bday="7", bmonth="July",
                byear="2007", aday="8", amonth="August", ayear="2008"))