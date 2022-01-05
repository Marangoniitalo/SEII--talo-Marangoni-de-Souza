if True:
	print('Conditional was True')

if False:
	print('Conditional was True')

language = 'Python'
if language=='Python':
	print('Conditional was True')

language = 'Python'
if language=='Python':
	print('Language is Python')
else:
	print('No match')

language = 'Java'
if language=='Python':
	print('Language is Python')
else:
	print('No match')

language = 'Java'
if language=='Python':
	print('Language is Python')
elif language=='Java':
	print('Language is Java')
else:
	print('No match')

language = 'Java'
if language=='Python':
	print('Language is Python')
elif language=='Java':
	print('Language is Java')
elif language=='JavaScript':
	print('Language is JavaScript')
else:
	print('No match')

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False
if not logged_in:
	print('Please Log In')
else:
	print('Welcome!')

a = [1,2,3]
b = [1,2,3]
c = b

print(a==b)
print(a is b)
print(b is c)
print(b == c)
print(id(a))
print(id(b))
print(id(c))

contidion = False
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = None
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = 0
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = 10
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = []
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = ''
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = {}
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')

contidion = 'Test'
if contidion:
	print('Evaluated to True')
else:
	print('Evaluated to False')