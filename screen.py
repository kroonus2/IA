# -*- coding: utf-8 -*-
# Autor: Jefferson Beethoven Martins - adaptado de José Ricardo Gonçalves Manzan.
import os
import numpy as np
import random as rd

print("\x1b[2J\x1b[1;1H")
os.chdir(r'C:\\Users\\CAUPT - ALUNOS\\Documents\\ExemploMadaline')

#Carregamento das entradas.
entAux = np.loadtxt('Ent.txt')
(padroes,entradas) = np.shape(entAux) #Serão 7 letras de 63 entradas cada.

#Carregamento das saídas.
targAux = np.loadtxt('Targ.csv',delimiter=';',skiprows=0)
(numSaidas,targets)=np.shape(targAux) #Teremos 7 saídas.

limiar = 0.0
alfa = 0.01
errotolerado = 0.01
v = np.zeros((entradas,numSaidas)) # Pesos[63][7]
for i in range(entradas):
    for j in range(numSaidas):
        v[i][j]=rd.uniform(-0.1,0.1)
    #end.
#end.
    
v0 = np.zeros((numSaidas)) # V0[7] Um bias para cada saída.
for j in range(numSaidas):
    v0[j]=rd.uniform(-0.1,0.1)
#end.

# Saídas calculadas pela rede.
yin = np.zeros((numSaidas,1))
y = np.zeros((numSaidas,1))

erro = 1
ciclo = 0

while erro>errotolerado:
    ciclo = ciclo+1
    erro = 0
    for i in range(padroes):
        padraoLetra = entAux[i,:] # Um padrão completo (letra) será arrancado.
        
        for m in range(numSaidas):
            soma = 0
            for n in range(entradas):
                soma = soma + padraoLetra[n]*v[n][m] #Entrada x peso.
            #end.    
            yin[m] = soma + v0[m]
        #end    
        
        for j in range(numSaidas):
            if yin[j] >= limiar:
                y[j] = 1.0
            else:
                y[j] = -1.0
           #end
        #end
        
        # O vetor coluna de Target é uma saída.
        for j in range(numSaidas):
            erro = erro + 0.5*((targAux[j][i]-y[j])**2)
        #end
        
        # Os pesos antigos devem ser guardados.
        vanterior = v
        
        # A atualização dos pesos e bias deve ser feita a cada ciclo.
        for m in range(entradas):
            for n in range(numSaidas):
                v[m][n] = vanterior[m][n]+alfa*(targAux[n][i]-y[n])*padraoLetra[m]
            #end
        #end
        v0anterior = v0

        for j in range(numSaidas):
            v0[j] = v0anterior[j] +alfa*(targAux[j][i]-y[j])
        #end    
    #end
    print(ciclo)
    print(erro)
#end

# Teste
# Rede treinada com sucesso.
entTeste=  entAux[6,:] # Uma letra é desginada aleatoriamente.
for j in range(numSaidas):
    soma = 0
    for i in range(entradas):
        soma = soma + entTeste[i]*v[i][j]
    #end    
    yin[j] = soma + v0[j]
#end

print(yin)
for j in range(numSaidas):
    if yin[j]>=limiar:
        y[j]=1.0
    else:
        y[j]=-1.0
    #end
#end    
print(y)
