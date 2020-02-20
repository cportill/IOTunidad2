#Cristhian Alejandro Frias Portillo
#longitud_cadena

x = input("Escriba la palabra: ")

def longitud(x):
  contador=0
  for i in x:
    contador+=1
  return contador

print((x),"tiene",longitud(x),"caracteres")
