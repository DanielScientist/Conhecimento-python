#Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python.

from configparser import Interpolation, InterpolationDepthError


n1=input('digite um valor ')
n2=input('digite um novo valor ')
t=s1+s2
print('a soma total é {}'.format(t)) 


#o codigo acima há um erro onde a soma envês de dá 10 está dando 55, sem o tipo primitivo invês de somar ele vai apenas concatinar (juntar) os numeros.

#um exemplo de tipo primitivo é o int, tudo o que tiver dentro do int sera convertido em um numero inteiro

n1=int(input('digite um numero: '))
n2=int(input('digite um novo numero: '))
s=n1+n2
print('resultado final é {}'.format(s))


#alguns dos tipos primitivos são

int=numero Inteiro (5,8,3,4,2,8,-4 etc)
floot=numeros reais ou flutuantes (4.6,4.855,368.434)
bool=(True e False)
str='olá'