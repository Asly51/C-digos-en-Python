#Se quiere crear un programa que calcule el área de un rectángulo (a = bxh) r indique si el área es mayor a 40 y su altura es mayor a 10 muestre un mensaje personalizado en pantalla area de un rectangulo 
#Se le indica al usuario que especifique los valores de la base y la altura
base =float (input ("Ingrese el valor de la base:"))
altura =float (input ("Ingrese el valor de la altura:"))
#Explicamos el procedimiento que se realizara
area = base*altura
#El programa emitira un mensaje en la pantalla con el resultado 
print (f"El area es de: {area}")
#Aplicamos las condiciones 
if area >= 40 and altura >= 10:
    print ("El resctangulo es grande XD")
else:
    print ("Es dificil procesar la informacion en estos momentos ya que el area y la altura no coinciden con las condiciones, BYE")