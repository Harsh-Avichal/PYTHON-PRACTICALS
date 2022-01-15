'''
Name : Harsh Avichal
ID   :   20CS005
Aim  : Write a Python script to concatenate following dictionaries to create a new one.
'''

# Dictionary dic1
dic1 = {1:10,2:20}
# Dictionary dic2
dic2 = {3:30,4:40}
# Dictionary dic3
dic3 = {5:50,6:60}
# Empty Dictionary dic4
dic4 = {}
for d in (dic1,dic2,dic3) : dic4.update(d)
print(dic4)