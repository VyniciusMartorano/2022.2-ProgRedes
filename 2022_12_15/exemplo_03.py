import socket, sys

host = 'www.globo.com'

var_1, var_2, var_3 = socket.gethostbyname_ex(host)

print(var_1)
print(var_2)
print(var_3)