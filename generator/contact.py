from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
out = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " "*10 #Отключение небезопасных символов
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(
        firstname=random_string("firstname", 15),
        lastname=random_string("lastname", 15),
        home=random_string("homephone", 15),
        mobile=random_string("mobilephone", 15),
        work=random_string("workphone", 15),
        fax=random_string("fax", 15),
        phone2=random_string("phone2", 15),
        email=random_string("email", 15),
        email2=random_string("email1", 15),
        email3=random_string("email2", 15),
    )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
