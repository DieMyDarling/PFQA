# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contacts(app):
    app.login(username="admin", password="secret")
    app.fill_form(Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname",
                                   nickname="test_nickname", title="test_title", company="test_company",
                                   home="test_home",
                                   address="test_address", mobile="test_mobile", work="test_work", fax="test_fax",
                                   email="test_email", email2="test_email2", email3="test_email3",
                                   homepage="test_homepage",
                                   notes="test_notes", phone2="test_phone2", address2="test_address2",
                                   bmonth="January", bday="1", byear="2000", amonth="February", aday="2", ayear="2002"))
    app.logout()