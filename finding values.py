courses = ['maths', 'physics', 'chemistry', 'biology']

print(courses.index('physics')) #index of the input
print('art' in courses) #to know whether the input is in the list

for item in courses:  #for loop for printing every item in the list, and you can rename item as anything, like course
    print (item) 

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start= 1): #a start value can be assigned like so to start from 1 instead of 0
    print(index, course)

courses_str = ' - '.join(courses) #this is used to make the list into a string separated by ", " bw each value
print(courses_str)

new_list = courses_str.split(' - ') #this makes the string back into a list by removing the " - "
print(new_list)