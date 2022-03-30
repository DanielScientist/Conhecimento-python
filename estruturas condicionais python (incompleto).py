#Como Usar as Estruturas Condicionais no Python

#Antes de partir para a prática é bom entender o que é uma estrutura condicional, isso é bem simples, mas é importante que entenda bem!

#Uma estrutura condicional, como o próprio nome já diz é uma estrutura que vai analisar uma condição e baseado no resultado dessa condição é que vamos executar uma determinada ação.

#Vamos iniciar com a função IF, traduzindo ela significa SE. Então fica mais fácil de entender.

#Um exemplo simples, SE 10 for maior que 5, então vamos executar uma ação, caso contrário não vamos fazer nada.

#Então a função IF vai executar uma ação somente se a condição testada for verdadeira, nesse caso vai executar tudo que estiver dentro dela (com a indentação, espaçamento que temos abaixo do IF para mostrar que as informações fazem parte dele).

nome='daniel'
sobrenome=''
lista=[]

if nome:
    print('a variavel nome não é vazia')

if sobrenome:
    print('a variavel sobrenome não é vazia')

    #Estrutura IF

#Aqui temos um exemplo bem simples para iniciar e já te mostrar a estrutura da função. Estamos definindo 2 variáveis e uma lista.

# abaixo temos duas funções IF para que você veja o que acontece. Na primeira quando deixamos somente if + a variável o Python vai verificar se essa variável é vazia ou não.

#Ou seja, nesse caso ele só vai fazer a verificação se temos informação ou não dentro dessa variável.

#Como temos 2 funções IF, as duas estão fazendo a mesma verificação, mas perceba que temos somente 1 resultado.

#Nesse caso a variável nome tem uma informação, que é Daniel, então é verdadeiro, pois temos algo dentro da variável.

#No segundo caso, como não temos informação o Python vai ver que a variável é vazia, portanto, não temos nada e com isso o resultado é falso.

#Como o resultado é falso o Python não vai passar pelo código que está dentro do IF, ou seja, tudo que está dentro do IF será desconsiderado.

#Isso quer dizer que só vamos ter o código dentro do IF sendo executado se a condição for verdadeira, caso contrário ele vai simplesmente pular esse código e passar para a próxima linha de código que esteja fora dessa estrutura.

#Antes de ir para os próximos exemplos vamos aprender como usar operadores lógicos no Python, pois eles vão te ajudar muito nessas funções para poder fazer suas comparações.

var = 5

if var == 5:
    print('Os valores são iguais')

if var != 7:
    print('O valor não é igual a 7')

if var > 2:
    print('O valor da variável é maior de 2')

if var >= 5:
    print('O valor da variável é maior ou igual a 5')

if var < 7:
    print('O valor da variável é menor que 7')

if var <= 5:
    print('O valor da variável é menor ou igual a 5')
    

#Agora você vai ter uma noção melhor de como utilizar o IF sem apenas verificar se temos ou não informação na variável.

#Agora podemos fazer comparações se um valor ou texto é igual ao outro, se um valor é maior, menor, igual… E assim fazer comparações mais específicas.


    #ELSE

    valor1=10
    valor2=20

    if valor1 > valor2:

        print('o valor1 é maior que o valor2')

        else:
            print('o valor2 é maior que o valor1')

#Estrutura ELSE

#Aqui temos outro exemplo já utilizando a função ELSE (que seria o senão). Isso quer dizer que vamos primeiramente testar a informação do IF e se ela não for verdadeira nós vamos para essa opção.

#Dessa forma teremos 2 resultados para essa nossa comparação, um para verdadeiro e um outro para falso.

#Nesse caso é possível observar que fizemos uma comparação entre 2 números, e como a primeira comparação é falsa, ele já foi para o ELSE.

#Então você vai ler, se valor1 é maior do que o valor2, então executa o que está dentro do IF, se não executa o que está dentro do ELSE.

#Só que algumas vezes nós precisamos de mais de 2 resultados, como por exemplo um semáforo de trânsito.

#Se tivermos verde, quer dizer que podemos passar, mas no amarelo já precisamos de atenção e no vermelho precisamos parar.

#Então ao invés de utilizar 3 vezes a função IF ou usar IF ELSE e depois outro IF, nós temos a função ELIF, que seria basicamente a junção de um ELSE + IF.

cor='alguma cor'
if cor =='verde':
    print('acelerar')
elif cor=='amarelo'
print('atenção')
else:
    print('parar')

    #Estrutura ELIF

#Aqui temos uma variável com um texto e temos 2 opções, mas com 3 resultados. Primeiro vamos verificar se o texto é verde, se for temos o resultado acelerar.

#Se o texto não for verde, nós vamos para a segunda comparação que é amarelo, então se for verdadeiro, teremos o resultado atenção. Junção do ELSE já que o primeiro não é verdade com um IF, pois vamos dar continuidade as verificações.

#Por fim, temos o ELSE (senão), que independe da informação que temos, pois o ELSE ele só vai ser executado se as opções anteriores forem falsas, então é basicamente o que sobra.

#Então se não é verde nem amarelo só poderia ser vermelho, então o resultado seria parar.

#OBS: Nesse caso você percebeu que mesmo colocando um texto qualquer nós tivemos o resultado do que seria o semáforo em vermelho. Isso acontece por conta do ELSE e porque não colocamos nenhum outro IF para verificar se o texto é de fato vermelho.

#Então é muito importante que você sempre verifique se está cobrindo todas as possibilidades para que não tenha um resultado errado.

#Você vai ver muito isso quando estiver debugando (verificando por erros) um código, vai verificar se os resultados estão de acordo com o que precisa.

#Nesse caso poderíamos ter colocado outro ELIF para verificar se o texto é vermelho e dentro do ELSE informar que a informação não é válida ou algo do tipo.

