"""
Resolução de sistemas lineares pelo método do escalonamento (Gauss-Jordan)

Este programa lê um sistema linear (matriz aumentada) da entrada padrão
e identifica automaticamente se o sistema é:
- Sistema Possível Determinado (S.P.D)
- Sistema Possível Indeterminado (S.P.I)
- Sistema Impossível (S.I)

Exemplo de entrada (para 3 variáveis x, y, z):

a b c p
d e f q
g h i r
"""

M=[]  # matriz aumentada do sistema

def escalonar(col):
    """Elimina os coeficientes abaixo do pivô na coluna 'col'."""
    for j in range(len(M)-(col+1)):
        multiplicador=M[j+1+col][col]
        for i in range(len(M[0])):
            M[j+1+col][i]+=M[col][i]*(-multiplicador)

def simplificar(den):
    """Divide a linha 'den' pelo pivô (tornando-o igual a 1)."""
    denominador=M[den][den]
    for i in range(len(M[0])):
        if denominador!=0.0:
            M[den][i]/=denominador

def escalonar_inversamente(col):
    """Elimina os coeficientes acima do pivô na coluna 'col'."""
    for j in range(col-1,-1,-1):
        multiplicador=M[j][col]
        for i in range(len(M[0])-1,-1,-1):
            M[j][i]+=M[col][i]*(-multiplicador)

# Leitura da matriz aumentada
while True:
    try:
        linha = list(map(float,input().split()))
        M.append(linha)
    except EOFError:
        break

linhaAC_nula=[0.0]*len(M[0])
linhaA_nula=[0.0]*(len(M[0])-1)

postoAC=0
postoA=0

# Escalonamento direto
for i in range(len(M)):
    simplificar(i)
    if i<len(M)-1:
        escalonar(i)

# Cálculo dos postos
for fila in M:
    if fila==linhaAC_nula:
        postoAC+=1
    if fila[:-1]==linhaA_nula:
        postoA+=1

# Análise do tipo de sistema
if postoA!=postoAC:
    print('Sistema Impossível (S.I)')
    print('Solução: vazio')
elif len(M[0])-1>len(M)-postoAC:
    print('Sistema Possível Indeterminado (S.P.I)')
    print('Solução: infinitas')
else:
    for u in range(len(M)-1,-1,-1):
        escalonar_inversamente(u)
    print('Sistema Possível Determinado (S.P.D)')
    solucao = [f'{M[i][-1]:.2f}' for i in range(len(M))]
    print(f'Solução: ({', '.join(solucao)})')

        


