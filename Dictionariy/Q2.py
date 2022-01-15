'''
Name : Harsh Avichal
ID   :   20CS005
Aim  : Write a Python script to merge two Python dictionaries.
'''
# creating the d1 dictionary with two keys-pair Values.
d1 = {'a': 100, 'b': 200}
# creating the d2 dictionary with two keys-pair Values.
d2 = {'x': 300, 'y': 200}
# variable d that copies the value of d1
d = d1.copy()
# variable d merging d1 and d2 with update method.
d.update(d2)
print(d)