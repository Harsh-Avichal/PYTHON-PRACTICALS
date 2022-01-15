'''
Name : Harsh Avichal
ID   :   20CS005
Aim  : Write a Python script to check whether a given key already exists in a dictionary.
'''

# creating the dictionary with certain key and pair.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# function is_key_present
def is_key_present(x):
    #checking the condition for key to be present in given dictionary.
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)