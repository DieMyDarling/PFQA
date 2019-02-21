from model.group import Group
from random import choice


def test_mod_group_by_id(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    old_groups = db.get_group_list()
    group = choice(old_groups)
    group_mod = Group(name="New group1", header="New header1", footer="New footer1")
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    #assert len(old_groups) == len(new_groups)
    pos = old_groups.index(group)
    old_groups[pos] = group_mod
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Test", header="", footer=""))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="New group1", header="New header1", footer="New footer1")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=New header))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)