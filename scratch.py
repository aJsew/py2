# 1
print(bytearray('разработка'.encode()))
print(bytearray('сокет'.encode()))
print(bytearray('декоратор'.encode()))
print(bytearray("""\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430""".encode()))
print(bytearray('\u0441\u043e\u043a\u0435\u0442'.encode()))
print(bytearray("""\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440""".encode()))
# В байтовом виде записаны одинаково(юникод-закодированое и обычное слово)

# 3
print(bytearray('функция'.encode()))
print(bytearray('класс'.encode()))
print(bytearray('type'.encode()))
print(bytearray('attribute'.encode()))
# type и attribute записаны буквами, класс и функция кодировками

# 4
print((bytearray('разработка'.encode())).decode())
print((bytearray('разработка'.encode())).decode())
print((bytearray('разработка'.encode())).decode())
print((bytearray('разработка'.encode())).decode())

# 2

print(bytes('class', encoding='utf-8'))
print(bytes('function', encoding='utf-8'))
print(bytes('method', encoding='utf-8'))





