courses = ['maths', 'physics', 'chemistry', 'biology']

nums = [1, 5, 2, 4, 3]

courses.reverse() #to reverse list
print (courses)

courses.sort() #to sort alphabetically
nums.sort() #to sort ascending
print(nums)
print(courses)

courses.sort(reverse = True) #sorts in reverse alphabetical or descending order
nums.sort(reverse = True)
print(nums, courses)

sorted_courses = sorted(courses)
print(courses)
print(sorted_courses) #this can be used to separately sort a variable without chaing the original one as shown

print(min(nums), max(nums)) #min and max of a list

print (sum(nums))