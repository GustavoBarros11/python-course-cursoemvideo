value = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(value))
print('Só tem espaços?', value.isspace())
print('É um numero?', value.isnumeric())
print('É alfabético?', value.isalpha())
print('É alfanumérico?', value.isalnum())
print('Está em maiusculas?', value.isupper())
print('Está em minusculas?', value.islower())
print('Está capitalizado?', value.istitle())