import random
import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_home_page.home) == clear(contact_from_edit_page.home)
    assert clear(contact_from_home_page.work) == clear(contact_from_edit_page.work)
    assert clear(contact_from_home_page.mobile) == clear(contact_from_edit_page.mobile)
    assert clear(contact_from_home_page.phone2) == clear(contact_from_edit_page.phone2)

def test_contact(app):
    contacts = list(app.contact.get_contact_list())
    index = random.randrange(len(contacts))
    contact_from_list = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_list.address == contact_from_edit_page.address
    assert contact_from_list.firstname == contact_from_edit_page.firstname
    assert contact_from_list.lastname == contact_from_edit_page.lastname
    assert '\n'.join(map(clear, contact_from_list.all_emails.split('\n'))) == "%s\n%s\n%s" % (
        clear(contact_from_edit_page.email), clear(contact_from_edit_page.email2), clear(contact_from_edit_page.email3))
    assert '\n'.join(map(clear, contact_from_list.all_phones.split('\n'))) == "%s\n%s\n%s\n%s" % (
        clear(contact_from_edit_page.home), clear(contact_from_edit_page.mobile),
        clear(contact_from_edit_page.work), clear(contact_from_edit_page.phone2))


def clear(s):
    return re.sub("[-+@ ()]", "", s)
