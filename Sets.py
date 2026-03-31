# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} 
print (cs_courses) #a set does not care about the order of arrangement, and it does not repeat values.
print('Math' in cs_courses) #lists and tuples also do this, but it is optimized for sets.

art_courses = {'History', 'Math', 'Art', 'Design',} 

print(cs_courses.intersection(art_courses)) #used for common items.
print(cs_courses.difference(art_courses)) #used for different items.

print(cs_courses.union(art_courses)) #all items from both sets



#empty lists
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty set
empty_set = {} #this isn't right! this is a dictionary! it is correct for the other cases tho.
empty_set = set() #correct