#Primeramente declaramos el precio de los zapatos
precio = 80

#Le damos la bienvenida al usuario
print ("Bienvenido al programa de la tienda de zapatos")
cantidad = int(input ("Puedes ingresar la cantidad de zapatos que deseas comprar:"))

#Especificamos los valores
Total = cantidad

#Declaramos las condiciones
if 10 <= cantidad < 20:
    descuento = 0.1
    
elif 20 <= cantidad < 30:
    descuento = 0.2
    
elif cantidad >= 30:
    descuento = 0.4
    
else:
    descuento = 0

#Declaramos las operaciones
Total_de_compra = cantidad*precio
Descuento = Total_de_compra*(1-descuento)

#Finalizamos con un mensaje
print ("El total de compras con el descuento es de:  $", Descuento)
