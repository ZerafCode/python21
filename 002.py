from prettytable import PrettyTable
title_name = 'Python Keywords List'
print(title_name.center(100))
keyword_table = PrettyTable()
keyword_table.add_column('keywords', ['False', 'break', 'for', 'not'])
keyword_table.add_column('keywords', ['or', 'None', 'class', 'from'])
keyword_table.add_column('keywords', ['async', 'except', 'lambda', 'with'])
keyword_table.add_column('keywords', ['await', 'finally', 'nonlocal', 'yield'])
keyword_table.add_column('keywords', ['assert', 'else', 'is', 'while'])
keyword_table.add_column('keywords', ['True', 'continue', 'global', 'pass'])
keyword_table.add_column('keywords', ['and', 'del', 'import', 'return'])
keyword_table.add_column('keywords', ['as', 'elif', 'in', 'try'])
keyword_table.add_column('keywords', ['__peg_parser__', 'def', 'if', 'raise'])
print(keyword_table)




