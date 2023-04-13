ls = [2, 3, 55, 66, "ram", "22"]

# in some function of list it will not give the duplicate list it
# will modify the original list and return it
print(int(ls.pop())+4)
print(ls.pop())
print(ls)
dd = ['ram', 44, 445, 4.4]
dd.remove(44)
ls.append(dd)
print(ls)
# index tells us the index position of that value
print(ls.index(66))
print(ls)
print(ls)
ds = ls.copy()
ds.clear()
ls.clear()
print(ls)
print(ds)

# here we casefold this str but string is immutable it will not
# modify the existing str and not changes the value of the original str
'''
name = "Raja"
# and here .casefold() will return the new string
print(name.casefold())  # "raja"
# here it doesn't change the value of name
print(name)  # "Raja"
'''