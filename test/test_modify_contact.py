# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first(Contact(firstname="test_firstname1", middlename="test_middlename1", lastname="test_lastname1",
                                    nickname="test_nickname1", title="test_title1", company="test_company1",
                                    home="test_home1",
                                    address="test_address1", mobile="test_mobile1", work="test_work1", fax="test_fax1",
                                    email="test_email_1", email2="test_email2_2", email3="test_email3_3",
                                    homepage="test_homepage1",
                                    notes="test_notes1", phone2="test_phone3", address2="test_address3",
                                    bmonth="July", bday="7", byear="2007", amonth="August", aday="8", ayear="2008"))