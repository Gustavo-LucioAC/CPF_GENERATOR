import random
cpf = []
estado = str(input('Qual o estado onde você mora: '))

def gera_num():
    for n in range(0,11):
        cpf_num = random.randint(0, 9)
        cpf.append(cpf_num)
    print(cpf)
    

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


gera_num()
nonodig(estado)
pdv()
sdv()

while sum(cpf) != 33 and sum(cpf) != 44 and sum(cpf) != 55:
    gera_num()
    nonodig(estado)
    pdv()
    sdv()
    
print(f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')