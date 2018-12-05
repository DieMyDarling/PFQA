from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    old_groups = app.group.get_group_list()
    group = Group(name="New group1", header="New header1", footer="New footer1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=New header))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)