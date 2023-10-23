# CPF_GENERATOR

Um gerador de CPFs válidos para todas as regiões do Brasil

## Como funciona:

* Inicialmente, são gerados 11 números de forma aleatória (de 0 a 9)
* Em sequência é pedido ao usuário que informe um estado (MG,SP,ES,RJ,MT e etc...)
* Depois é feito um cálculo para gerar o 10 número do CPF, sendo ele o primeriro digíto verificador
* Em sequeência, é feito o cálculo do 11 número, o segundo dígito verificador
* E se todos os dados estiveremcorretos é feita uma vericação, na qual a soma de todos os número do CPF tem que dar 33, 44, 55 ou 66


## Geração dos números

Foi usada a bibliteca random para se gerar os 11 números inicialmente

```py
import random
cpf = []
estado = str(input('Qual o estado onde você mora: '))

def gera_num():
    for n in range(0,11):
        cpf_num = random.randint(0, 9)
        cpf.append(cpf_num)
    print(cpf)
```

## Seleção do estado desejado / Definição do 9 número

Aqui o usuário escolhe um estado no qual ele quer gerar um CPF válido:


|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |
|----|----|----|----|----|----|----|----|----|
| DF | AC | CE | AL | BA | MG | ES | SP | PR |
| GO | AM | MA | PB | SE |    | RJ |    | SC |
| MS | AP | PI | PE |    |    |    |    |    |
| MT | PA |    | RN |    |    |    |    |    |
| TO | RO |    |    |    |    |    |    |    |
|    | RR |    |    |    |    |    |    |    |

Pode-se observar que os estados possuem números diferente, números esses que correspondem ao 9 dígito do CPF


```py
def nonodig(estado):
    if estado == 'DF' or estado == 'GO' or estado == 'MT' or estado == 'MS' or estado == 'TO':
        cpf[8] = 1
    if estado == 'PA' or estado == 'AM' or estado == 'AC' or estado == 'AP' or estado == 'RO' or estado == 'RR':
        cpf[8] = 2
    if estado == 'CE' or estado == 'MA' or estado == 'PI':
        cpf[8] = 3
    if estado == 'PE' or estado == 'RN' or estado == 'PB' or estado == 'AL':
        cpf[8] = 4
    if estado == 'BA' or estado == 'SE':
        cpf[8] = 5
    if estado == 'MG':
        cpf[8] = 6
    if estado == 'RJ' or estado == 'ES':
        cpf[8] = 7
    if estado == 'SP':
        cpf[8] = 8
    if estado == 'PR' or estado == 'SC':
        cpf[8] = 9
    if estado == 'RS':
        cpf[8] = 0
```

## Geração do 10 número (primeiro número verificador)
```py
def pdv():
    cp_cpf = cpf[:]
    for i in range(len(cp_cpf)-2):
        cp_cpf[i] = cp_cpf[i] * (10-i)
    num_v1 = sum(cp_cpf[0:9])%11

    if num_v1 < 2:
        num_v1 = 0
        cpf[9] = num_v1
  
    else:
        num_v1 = 11 - num_v1
        cpf[9] = num_v1
```

Para se calcular o 10 número, os número anteriores são multiplicados numa fatorial de 10, como no exepmplo a seguir: 

| n1 | n2 | n3 | n4 | n5 | n6 | n7 | n8 | n9 |
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
| x10| x9 | x8 | x7 | x6 | x5 | x4 | x3 | x2 |

Em seguida, esses números são somados e seu resultado dividido por 11

EX:

```ruby
10 + 36 + 40 + 21 + 48 + 10 + 8 + 0 + 12 = 185
```

Novamente vamos efetuar a divisão por 11 usando o módulo:

```ruby
185 % 11 = 9
```

Agora iremos cálcular o dígito verificador:

```ruby
11 - 9 = 2
```

* Se o resto dessa divisão for < 2, o 10 número automáticamente se torna 0
* Do contrário, é pego o resto desta divisão e subtraido de 11 para se obter o número

## Geração do 11 número (segundo número verificador)

```py
def sdv():
    cp_cpf = cpf[:]
    for i in range(len(cp_cpf)-1):
        cp_cpf[i] = cp_cpf[i] * (11-i)
    num_v2 = sum(cp_cpf[0:10])%11

    if num_v2 < 2:
        num_v2 = 0
        cpf[10] = num_v2

    else:
        num_v2 = 11 - num_v2
        cpf[10] = num_v2
```

  
Para se calcular o 11 número, os número anteriores são multiplicados numa fatorial de 10, como no exepmplo a seguir: 

| n1 | n2 | n3 | n4 | n5 | n6 | n7 | n8 | n9 | n10 |
|--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| x11| x10 | x9 | x8 | x7 | x6 | x5 | x4 | x3 | x2 |

Em seguida, esses números são somados e seu resultado dividido por 11

EX:

```ruby
11 + 40 + 45 + 24 + 56 + 12 + 10 + 0 + 18 + 4 = 220
```

Novamente vamos efetuar a divisão por 11 usando o módulo:

```ruby
220 % 11 = 0
```

* Se o resto dessa divisão for < 2, o 10 número automáticamente se torna 0
* Do contrário, é pego o resto desta divisão e subtraido de 11 para se obter o número

## Validador

Para validar o CPF, é necessário que a soma de todos os seus números dê 33, 44, 55 ou 66:

```py
while sum(cpf) != 33 and sum(cpf) != 44 and sum(cpf) != 55 and sum(cpf) != 66:
    gera_num()
    nonodig(estado)
    pdv()
    sdv()
```

Caso a soma nâo dê um desses valors, são chamadas as funções de formaçâo novamente


