# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:14:49 2022

@author: Fabian
"""
# Crear un vector de datos
vector1=[2,1,3,4,5,6]
print (vector1)
print("Los elementos del vector son: " + str(vector1))
print("La cantidad de elementos del vector son: " + str(len(vector1)))

for i in vector1:
    print(i)

vector1.append(88)
vector1.sort() # Ordena de Menor a Mayor
print(vector1)    

vector1.sort(reverse=True) # Ordena de Mayor a Menor
print(vector1)

vector1.remove(2)
print(vector1)
vector1.insert(1,2) # posición y elemento a insertar
print(vector1)

# Crear una Matriz Bidimencional
matriz1=[(1,2,3),(5,6,7)]
# 1 2 3
# 5 6 7
print (matriz1)

for i in matriz1:
    print(i)

# Crear una Matriz Bidimencional de 3x3
matriz2=[(1,2,3),(4,5,6), (7,8,9,88)]
# 1 2 3
# 4 5 6
# 7 8 9

print (matriz2)

for i in matriz2:
    print(i)

# otra forma de recorrer la matriz
for i in range(len(matriz2)):
    print(matriz2[i], "\n",end="")
    
#Matrices Multidimensionales
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M)
for i in range(len(M)):
    for j in range(len(M[i])):
        #print (i)
        print(M[i][j], "\n", end="")
# Para i
# 0 --> [1,2,3]
# 1 --> [4,5,6]
# 2 --> [7,8,9]

# for j in range(len(M[i])):
# j0 --> 1 - 4 - 7
# j1 --> 2 - 5 - 8
# j2 --> 3 - 6 - 9
#........
        
M2=[[(1,2,3),(4,5,6)],[(7,8,9),(11,12,13)],[(14,15,16),(17,18,19)]]
#print(M2)
for i in range(len(M2)):
    for j in range(len(M2[i])):
        for w in range(len(M2[i][j])):
            #print (i)
            print(M2[i][j][w], "\n", end="")
M2[1].append("BELEN")
print(M2)            
M2[0].remove("Fabi")
print(M2)

M2[2].insert(1,"Caro")
print(M2) 


