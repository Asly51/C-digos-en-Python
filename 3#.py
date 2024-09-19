#El Banco Consolidado de la República le requiere un programa que almacene una contraseña en una variable, pregunte al usuario por la contraseña e imprima si la contraseña introducida coincide con la guardada en la variable (sin tener en cuenta mayúsculas y minúsculas).
#Interactuamos con el usuario 
nombre = input ("Ingrese su nombre:")
print (f"Hola, {nombre},Comencemos a craer tu cuenta")
# Le pidimos el nombre de la cuenta y la contraseña
usuario = input("Introduce el nombre de la cuenta:")
contraseña_usuario = input("Introduce la contraseña: ")
print("Cuenta creada exitosamente.")

#Pedimos al usuario que ingrese a su Cuenta
print("Ingrese a su cuenta nuevamente")
cuenta = input("Introduce el nombre de la cuenta:")
contraseña = input("Introduce la contraseña: ")

# Observamos y analizamos si la contraseña introducida es la  misma que la original
if contraseña == contraseña_usuario and cuenta == usuario:
    print(f"Datos validos, Bienbenid@ {nombre}")
else:
    #Si la contraseña no es igual a la original entonces arrojara el siguiente mensaje
    print("Datos invalidos.")