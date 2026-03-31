student = {'name': 'Ishita', 'age': '19', 'courses': ['Math', 'CompSci']} #curly bracks create a dictionary

print(student['name'])
print(student['courses'])
print(student.get('phone')) #this is another way to get the value of a key, but it is better than the previous one because if you try to get a key that doesn't exist, it will return None instead of giving an error.

print(student.get('phone','Not Found')) #It prints 'Not Found' because the key 'phone' doesn't exist in the dictionary, and we have provided a default value to return when the key is not found.

student.update({'name': 'Ishita S', 'age': 20, 'phone': '555-5555'}) #this is used to update the values of the keys, and also to add new key-value pairs to the dictionary.
print(student)
del student['phone'] #this is used to delete a key-value pair from the dictionary.
age = student.pop('age') #this is used to remove a key-value pair from the dictionary and return the value of the removed key. If the key doesn't exist, it will raise a KeyError.

print(student)
print(age)
print(len(student)) #this is used to get the number of key-value pairs in the dictionary.
print(student.keys()) #this is used to get a list of all the keys in the dictionary.
print(student.values()) #this is used to get a list of all the values in the dictionary.
print(student.items()) #this is used to get a list of all the key-value pairs in the dictionary as tuples.

for key in student:
    print(key) #this is used to loop through the keys in the dictionary.

for key, value in student.items():
    print(key, value) #this is used to loop through the key-value pairs in the dictionary. It unpacks the tuple into key and value variables.