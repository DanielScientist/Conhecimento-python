#Em Python, o método capitalize() converte o primeiro caractere de uma string em letras maiúsculas e todos os outros caracteres em minúsculas, se houver. 

m1=input('digite um texto: ')
print(m1.capitalize())

# método isalnum() retornará True se todos os caracteres da string forem alfanuméricos (alfabetos ou números). Se não, retorna False. 

m2=input('olá humanos escreva apenas letras ou numeros')
print(m2.isalnum())

#O método isalpha() retornará True se todos os caracteres da string forem alfabetos. Se não, retorna False.

m3=input('olá humanos por gentileza utilizar apenas letras')
print(m3.isalpha())

#O método isdecimal() retornará True se todos os caracteres em uma string forem caracteres decimais. Se não, retorna False. 

m4=input('olá humanos por gentileza utilizar apenas caracteres decimais')
print(m4.isdecimal())

#O isdigit()método retorna Truese todos os caracteres em uma string forem dígitos. Se não, ele retorna False. 

m5=input('por gentileza  escrever apenas digitos')
print(m5.isdigit())

#O método islower() retornará True se todos os alfabetos em uma string forem letras minúsculas. Se a string contiver pelo menos um alfabeto maiúsculo, ela retornará False. 

m6=input('escreva apenas letras minusculas')
print(m6.islower())

#O método isnumeric() retornará True se todos os caracteres em uma string forem caracteres numéricos. Se não, retorna False. 

m7=input('por gentileza escreva apenas caracteres numericos')
print(m7.isnumeric())

