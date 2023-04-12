# some string functions let's deep dive into it

# name = "Gaurav Rajput"
# name = "ramv Rajput"
#
# print(name.casefold())  # it will convert upper case into lower case
# print(name.isspace())
#
# here we can write a logic here for write a name like title first letter is capital and other will small
# print(name.istitle())


def title(name):
    if not name.istitle():
        name = name.title()
    return name


data = 'ram singh'


myname = title(data)
print(myname)