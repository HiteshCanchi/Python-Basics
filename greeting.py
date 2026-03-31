greeting = 'Hello'
name = 'vader'

message = greeting + ', ' + name + '. Welcome!'
print (message)

message = '{}, {}. Welcome!'.format(greeting, name) #curly brackets are used as placeholders
print(message)

message = f'{greeting}, {name}. Welcome!' #another method using f string
print (message)

message = f'{greeting}, {name.upper()}. Welcome!'
print (message)

print(help(str)) #used to find info on string (str)

print(help(str.lower)) #help for only what .lower does