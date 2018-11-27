from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_user(Contact(firstname="test_firstname1", bday="1", aday="2", amonth="January", bmonth="February"))
    app.contact.delete_first_contact()