import pymysql.cursors
from model.group import Group

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user="root", password="")

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer, from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
            return list


    def destroy(self):
        self.connection.close()