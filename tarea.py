import os
os.system('clear')
# Respuesta

#  def matriz_producto(A,x):
#      b = [0, 0, 0]
#      for i in range(0,len(A)):
#          for j in range(0,len(A)):
#              b[i] =  x[i] * A[i][j] + b[i]
#      return b
#
#  A = [[1,0,0],
#       [0,1,0],
#       [0,0,1]]
#
#  x = [1, 2, 3]
#
#  r = matriz_producto(A,x)
#  print(r)
#
#
#  #  for i in x:
#      #  for i in x:
#      #      index = i-1
#      #      # print(f'vector {x} y elemento {A[index]}')
#      #      print(f'{A[index][index]}')
#      #      #  suma = x*A[index] + suma
#      #
#  #  print(suma)
#

def matriz_producto(A,x):
    b = [0, 0, 0]
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i == 0:
                print(f'i = {i}')
                print(f'antes b = {b[i]}')
                b[i] =  (x[i] * A[i][j]) + b[i]
                print(f'resultado = {x[i]} * {A[i][j]}')
                print(f'despues b = {b[i]}')
                print(f'x={x[i]}')
                print(f'A={A[i][j]}')
            else:
                print(f'i = {i}')
                b[i] =  (x[i] * A[i][j]) + b[i-1]
                print(f'antes b = {b[i]}')
                print(f'resultado = {x[i]} * {A[i][j]}')
                print(f'despues b = {b[i]}')
                print(f'x={x[i]}')
                print(f'A={A[i][j]}')


    return b

A = [[1,19,10],
     [1,1,1],
     [1,1,1]]

x = [1, 2, 3]

r = matriz_producto(A,x)
print(r)

for i in range(0,len(A)):


