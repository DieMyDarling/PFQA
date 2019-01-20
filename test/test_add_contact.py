# -*- coding: utf-8 -*-
import random
import string
import pytest

from model.contact import Contact


def random_string(prefix, max_len=20):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

test_contact_data = [
    Contact(firstname=random_string("firstname", 15),
        lastname=random_string("lastname", 15),
        home=random_string("homephone", 15),
        mobile=random_string("mobilephone", 15),
        work=random_string("workphone", 15),
        fax=random_string("fax", 15),
        phone2=random_string("phone2", 15),
        email=random_string("email", 15),
        email2=random_string("email2", 15),
        email3=random_string("email3", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_contact_data, ids=[repr(x) for x in test_contact_data])
def test_contacts(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_user(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)