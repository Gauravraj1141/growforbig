school = {}
marks_cls1 = {'ram': 22, 'priya': 44, 'kalu': 55, 'ramon': 58}
marks_cls2 = {'divya': 22, 'priyanshi': 44, 'kalu': 55, 'ramon': 58}
name_cls3 = ['radha', 'priyanshu', 'ompal', 'kamlesh', 'titu']
mark_cls3 = [44, 33, 55, 77, 88]
marks_cls3 = dict(zip(name_cls3, mark_cls3))
school["marks_cls1"] = marks_cls1
school["marks_cls2"] = marks_cls2
school["marks_cls3"] = marks_cls3
# here we can add and update key value of  our dictionary
print(school['marks_cls1'].update(raman = 44))
print(school['marks_cls1'].setdefault('ram'))
print(school.get('marks_cls1'))
