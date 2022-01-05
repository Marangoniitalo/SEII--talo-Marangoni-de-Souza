print('Hello World')

message = 'Hello World'
print(message)

message = 'Bobby\'s World'
print(message)

message = "Bobby's World"
print(message)

message = """Bobbys's World
was a good cartoon in the 1990s"""
print(message)

message = 'Hello World'
print(len(message))

message = 'Hello World'
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])

message = 'Hello World'

print(message.lower())
print(message.upper())

message = 'Hello World'
print(message.count('Hello'))
print(message.count('l'))

print(message.find('World'))
print(message.find('Universe'))

print(message.replace('World', 'Universe'))

print(message)

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name}. Welcome!'
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))

#print(help(type(message)))
#print(help(str.lower)