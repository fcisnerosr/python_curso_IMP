import os
os.system('clear')
# Respuesta
A = [[1,0,0],
     [0,1,0],
     [0,0,1]]

x = [1, 2, 3]

suma = 0

for i in x:
    index = i-1
    print(f'vector {x} y elemento {A[index]}')
    #  suma = x*A[index] + suma
    
print(suma)


