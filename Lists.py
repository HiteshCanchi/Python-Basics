courses = ['maths', 'physics', 'chemistry', 'biology']

print(len(courses)) #you can use this to see the number of indices
print (courses[0]) #you can either use an index to specify which course you want to print, or if you don't use index, it just prints out the entire thing
print(courses[-1]) #negative values can be used to check the iten from the end

print(courses[0:2]) #from 0 to 2, but not including 2 instead of 0:2 u can also use :2
print(courses[2:]) #also called slicing.

courses.append('Art') #adds or appends the 'Art' to the end
print(courses)

courses.insert(0, 'History') #two arguments, first is the index and second is the value
print(courses)

courses_2 = ['Transfiguration', 'Potions']

#courses.insert (0, courses_2) #this can be used to insert a list within a list, but not just the contents of the list but the entire list itself
#print(courses)
#print (courses[0]) #this prints out the entire list rather than just the contents, which might not be what we need.

courses.extend(courses_2) #this can be used to simply add the contents of the list rather than the entire list
                          # if you use the append function, say append(courses_2) it'll still give you the entire list rather than its contents
print (courses)

courses.remove('maths') #to remove specific entires
print (courses)

popped = courses.pop() #removes last entry by default
print(popped) #you can see the popped entry
print(courses)
