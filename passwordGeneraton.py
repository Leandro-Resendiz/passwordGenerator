import random

chars = '!"#$%&/()*+,-/1234567890?¿@abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ'
password =''


lengthPW = int(input('¿Que longitud quieres para tu Contraseña:  '))

for _ in range(lengthPW):
    password += random.choice(chars)

print(password)

