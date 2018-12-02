# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contacts(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname")
    app.contact.create_user(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted (old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

