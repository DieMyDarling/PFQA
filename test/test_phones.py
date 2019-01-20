import random
import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails == merge_email_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)


# def test_contact(app):
#     contacts = list(app.contact.get_contact_list())
#     index = random.randrange(len(contacts))
#     contact_from_list = contacts[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_list.address == contact_from_edit_page.address
#     assert contact_from_list.firstname == contact_from_edit_page.firstname
#     assert contact_from_list.lastname == contact_from_edit_page.lastname
#     assert contact_from_list.all_emails == merge_email_like_on_homepage(contact_from_edit_page)
#     assert contact_from_list.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub(r"[^\d\+]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3])))
