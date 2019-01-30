# -*- coding: utf-8 -*-
import random
import string
import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " "*10 #Отключение небезопасных символов
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_group_data = [
    Group(name=random_string("name", 10),
          header=random_string("header", 20),
          footer=random_string("footer", 20))
    for i in range(3)
]


@pytest.mark.parametrize("group", test_group_data, ids=[repr(x) for x in test_group_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)