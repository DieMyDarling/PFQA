from sys import maxsize


class Contact:

    def __init__(self, title=None, company=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, firstname=None,
                 middlename=None, lastname=None, nickname=None, notes=None,
                 phone2=None, address2=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, all_phones=None, all_emails=None, id=None):
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.nickname = nickname
        self.notes = notes
        self.phone2 = phone2
        self.address2 = address2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname, self.lastname == other.lastname)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize