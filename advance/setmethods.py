s1 = {1,4,5,6,55,33,4,4,5,555,55,55,555,23,"dkd"}
s2 = {33,44444,54,44,55,66,5}
# it is a empty dictionary
a = {}
# it is a empty set
b = set()
# s1.clear()
# s1.remove(55)
# s1.union({7,6,88,56})
# print(s1.intersection(s2))
# print(s1.intersection_update(s2))
# it will update the existing set with intersection with another
# s2.intersection_update(s1)
# difference means that values are not common in both set
# print(s1.difference(s2))
# update will changes the value of existing set
# s1.difference_update(s2)
# remove the value of a set if it present in set other wise do nothing
#  s1.discard("dmkd")
# print(len(s1))
# if two sets have null intersection means no common value then it returns true
# print(s1.isdisjoint(s2))
s3 = {33,4}
# means s3 is the subset of s1
print(s3.issubset(s1))

print(s1.issuperset(s3))
# print(s1)
# print(s2)
