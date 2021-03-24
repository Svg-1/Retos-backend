from datetime import datetime


nombre = input("Ingresa tu nombre: ")
print ('Hola', nombre,)
edad = int(input("Ahora ingresa tu edad: "))

now = datetime.now()
hora = now.hour
minutos = now.minute
segundos = now.second


if (edad < 18 and hora >= 18):
    print("Tienes que hacer tus tareas")

else:
     print ('Eres mayor de edad, haz lo que quieras')











