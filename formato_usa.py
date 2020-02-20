#Cristhian Alejandro Frias Portillo
#formato_usa

cal = int(input("Ingresa calificación: "))

if cal <= 59:
    print("F")
    print("Reprobado")
elif cal >=  60 and cal<= 69:
    print("D")
    print("Poco satisfactorio")
elif cal>= 70 and cal<= 79:
    print("C")
    print("Bueno")
elif cal>= 80 and cal<= 89:
    print("B")
    print("Muy bueno")
elif cal>= 90 and cal<= 100:
    print("A")
    print("Excelente")
else:
    print("No")
