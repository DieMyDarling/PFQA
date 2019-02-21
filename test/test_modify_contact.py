# -*- coding: utf-8 -*-

from model.contact import Contact
from random import choice


def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_user(Contact(firstname="test_firstname1", bday="1", aday="2", amonth="January", bmonth="February"))
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)
    contact_mod = Contact(title="test_title1", company="test_company1", address="test_address1", home="test_home1",
                mobile="test_mobile1", work="test_work1", fax="test_fax1", email="test_email_1", email2="test_email2_2",
                email3="test_email3_3", homepage="test_homepage1", firstname="test_firstname1",
                middlename="test_middlename1", lastname="test_lastname1", nickname="test_nickname1",
                notes="test_notes1", phone2="test_phone3", address2="test_address3", bday="7", bmonth="July",
                byear="2007", aday="8", amonth="August", ayear="2008")
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contacts = db.get_contact_list()
    pos = old_contacts.index(contact)
    old_contacts[pos] = contact_mod
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


