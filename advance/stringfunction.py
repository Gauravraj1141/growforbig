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


data = '    ram    singh   '

# print(data.strip())
data.split()
# print(data)


myname = title(data)
# print(myname)


valuedata = "gaurav rajput,mca,99 k,23 years old"
keydata = "name,course,salary,age"

keylist = keydata.split(",")
valuelist = valuedata.split(",")
mydict = dict(zip(keylist,valuelist))
mydict['mynewname'] = "rajkumar"
mydict['name'] = "raja ji"
mydict['age'] = "28 years old"
print(mydict)
print(mydict['name'])
print(mydict['salary'])
print(mydict['course'])
print(mydict['age'])
# we can remove the substring from string
print(mydict['age'].rstrip('years old'))
print(mydict['age'].strip('years old'))

# we can concat dictionary with the help of | bitwise OR operator

report_type_data_ = dict(zip(['token'], [{'new_access_token': "ram"}]))
dict2 = {"type": 2, "type_name": "ram"}
concatss = report_type_data_ | dict2
print(concatss)  # {'token': {'new_access_token': 'ram'}, 'type': 2, 'type_name': 'ram'}



