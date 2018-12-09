# -*- coding: utf-8 -*-
import random
import string
import pytest

from model.contact import Contact


def random_string(prefix, max_len=20):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

test_contact_data = [
    Contact(firstname=firstname, lastname=lastname, home=home, work=work, phone2=phone2, email=email)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 20)]
    for home in ["", random_string("home", 20)]
    for work in ["", random_string("work", 20)]
    for phone2 in ["", random_string("phone2", 20)]
    for email in ["", random_string("email", 20)]
]


@pytest.mark.parametrize("contact", test_contact_data, ids=[repr(x) for x in test_contact_data])
def test_contacts(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_user(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)