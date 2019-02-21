from model.group import Group

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    print("ok")
