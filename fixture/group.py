class GroupHelper:


    def __init__(self, app):
        self.app = app


    def open_groups(self):
         wd = self.app.wd
         wd.find_element_by_link_text("groups").click()


    def submit(self):
         wd = self.app.wd
         wd.find_element_by_name("submit").click()


    def create(self, group):
         wd = self.app.wd
         self.open_groups()
         self.init_group_creation()
         self.fill_form(group)
         self.submit()
         self.return_to_group_page()


    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)


    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        # select_first_group
        wd.find_element_by_name("selected[]").click()
        # submit_deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()


    def modify(self, group):
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()


    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()


    def return_to_group_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("group page").click()