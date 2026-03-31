# mutable
list_1 = ['maths', 'physics', 'chemistry', 'biology']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'art'

print(list_1)
print(list_2)

# immutable
tuple_1 = ('maths', 'physics', 'chemistry', 'biology') #tuples can be used just to loop through, and access.
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'art' #tuples are immutable , i.e., it does not support assignment of values like list. Other than that, it's basically the same.

print(tuple_1)
print(tuple_2)