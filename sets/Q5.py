'''
Name : Harsh Avichal
ID   :   20CS005
Aim  : Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
'''
"""Write a Python program to find the most common elements and their counts from list, tuple, dictionary."""
# Creating a list and a tuple
List = [1, 2, 3, 2, 1, 1, 2, 4]
Tuple = (3, 4, 2, 1, 3, 3, 4, 2)


# Creating a function to get most common element
def common(a):
    # converting given datatype into set
    # and then maximizing the count of each element
    c = max(set(a), key=a.count)

    # Printing Most Common Element and its count
    print('Most Common Element is ', c, 'having count = ', a.count(c))


# Calling the function
common(List)
common(Tuple)