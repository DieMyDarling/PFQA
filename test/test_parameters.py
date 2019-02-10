import random
import string
import pytest

from model.contact import Contact
from model.group import Contact


def random_string(prefix, max_len=20):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + str([random.choice(symbols) for i in range(random.randrange(max_len))])

test_contact_data = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, home=home, work=work, phone2=phone2)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("middlename", 20)]
    for lastname in ["", random_string("lastname", 20)]
    for home in ["", random_string("home", 20)]
    for work in ["", random_string("work", 20)]
    for phone2 in ["", random_string("phone2", 20)]
]


test_group_data = [
    Contact(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

