message = 'welcome to python'
name = 'lina'
print(name, message)
print(name + message)
new_message = ", ".join((name, message))
print(new_message)
print('%s %s' % (name, message))
print('%s, %s! ' % (name, message))
print('<< %s, %s! >>' % (name, message))
number = 3
print('<< ' + name + ',😍 ' + (message) + str(3) + ' 👌')
print(f'{name}, {message} 3')
print('{} {}.'.format(name, message))
name += ', ' + message
print(name)

