# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contacts(app):
    app.contact.create_user(
        Contact(title="test_title", company="test_company", address="test_address", home="test_home",
                mobile="test_mobile", work="test_work", fax="test_fax", email="test_email", email2="test_email2",
                email3="test_email3", homepage="test_homepage", firstname="test_firstname",
                middlename="test_middlename", lastname="test_lastname", nickname="test_nickname", notes="test_notes",
                phone2="test_phone2", address2="test_address2", bday="1", bmonth="January", byear="2000", aday="2",
                amonth="February", ayear="2002"))