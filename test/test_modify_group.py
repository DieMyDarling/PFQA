from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="test2", header="test2", footer="test2"))
    app.session.logout()