def hellofunc():
	pass
print(hellofunc)
print(hellofunc())

def hellofunc():
	print('Hello function!')
hellofunc()

def hellofunc():
	return'Hello function.'
print(hellofunc())

print(hellofunc().upper())

def hellofunc(greeting):
	return'{} function.'.format(greeting)
print(hellofunc('Hi'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)
print(hellofunc('Hi'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)
print(hellofunc('Hi', 'Corey'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)
print(hellofunc('Hi', name = 'Corey'))

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
student_info('Math', 'Art', name='John', age=22)

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
courses = ['Math', 'Art']
info = {'name':'John', 'age':22}
student_info(courses, info)

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
courses = ['Math', 'Art']
info = {'name':'John', 'age':22}
student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):

    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))