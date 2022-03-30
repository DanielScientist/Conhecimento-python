# abaixo há um script que escreve um determinado texto no terminal

print('hello word')

# como o script abaixo não tem as aspas simples o quando executado não mostrarar o texto e sim o resultado.

print (7+8)

# com o script abaixo o terminal não me mostrará '7+4' e sim 74 pois o terminal vai entender que eu quis juntar os 2 numeros.

print('7'+'4')

#devemos aprender o que é uma variavel, variaveis são espaços onde guardamos alguma resposta ou funçoes, um exemplo é se eu quiser criar uma variavel com o nome 'endereço ' e em seguida eu escrever o nome da rua. exemplo:

endereco=('rua josé faustino')

#caso eu queira chamar essa variavel, chamarei o que tem dentro dela

print(endereco)

#agora vamos utilizar o comando input (que significa leia) o sistema vai receber a resposta do usuário e guardar em uma variavel

#exemplo

nome=input('qual é o seu nome?')

#o sistema guardou a resposta do usuario para usar futuramente como por exemplo

print('ola',nome,'é um prazer ter você aqui')

#invês de colocar por exemplo ''print('ola',nome,'é um prazer ter você aqui')'' podemos formatar diferente com o .format, exemplo.

#colocar variaveis demai com virgula acaba deixando o codigo feio.

print('olá é um prazer de te conhecer {}'.format(nome))