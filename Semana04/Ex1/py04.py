courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

print(len(courses))

print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])


courses.append('Art')
print(courses)

courses = ['hisory', 'math', 'physics', 'compsci']
courses.insert(0, 'Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort(reverse=True)
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

nums = [1, 5, 2, 4, 3]
print(min(nums))

nums = [1, 5, 2, 4, 3]
print(max(nums))

nums = [1, 5, 2, 4, 3]
print(sum(nums))

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))

courses = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses)
print('Math' in courses)

for index, course in enumerate(courses):
	print(index, course)

for index, course in enumerate(courses):
	print(index)
	print(course)

for index, course in enumerate(courses, start=1):
	print(index, course)


courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)
print(courses_str)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ' - '.join(courses)
print(courses_str)

new_list = courses_str.split(' - ')
print(new_list)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'art'
print(tuple_1)
print(tuple_2)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print('Math' in cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))	

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.difference(art_courses))	

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
print(type(empty_set))
empty_set = {} #This it's wrong. This is a dict.
print(type(empty_set))