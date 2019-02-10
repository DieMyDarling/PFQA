from model.group import Contact
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Contact(name="Test", header="", footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Contact(name="New group1", header="New header1", footer="New footer1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)



#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=New header))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)