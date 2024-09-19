#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad (18 años o más) o no.

#Interactuamos un poco con el usuario pidiendole su nombre
nombre = input ("¿Cual es tu nombre?")
#Al tener el nombre especificamos al usuario que coloque su edad
edad = int ( input("¿Que edad tienes?") )
#Le explicamos al programa el procedimiento que aplicará 
if edad >= 18:
   print (f"Felicidades eres mayor de edad, {nombre}")
#Si no se cumple la condición arrojará el siguiente mensaje 
else: 
   print (f"Aun te falta para ser mayor de edad, {nombre}")