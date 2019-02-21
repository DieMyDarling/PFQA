from model.contact import Contact
from random import choice


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_user(Contact(firstname="test_firstname1", bday="1", aday="2", amonth="January", bmonth="February"))
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
