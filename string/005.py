message = 'welcome to python'
name = 'lina'
new_message = '{} {}. wish a good time.'.format(name, message)
print(new_message)
print('{1} {0}. wish a good time.'.format(message, name))

print(f'{name} {message}. wish a good time.')
message_2 = '{}_{}_{}'.format('welcome', 'to', 'python')
print(message_2)
number = 5
print('total_number: {:,}'.format(number))
print('total_number: {:.002%}'.format(number))
print("decimal: {0:d}".format(number))
print("hex decimal: {0:x}".format(number))
print("octal: {0:o}".format(number))
print("binary: {0:b}".format(number))
print('exponent: {0:e}'.format(number))
print('rounding: {0:.2f}'.format(3/4))
message_3 = "| {:<5}|{:^5} |{:>5} |".format('welcome', 'to', 'python')
print(message_3)
#A string can be left (<), right(>) or center (^) justified with format method.like the above example