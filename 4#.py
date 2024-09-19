#En Corpoelec , los empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación son 0.0, 0.4, 0.6 o más. Escribe un programa que lea la puntuación del usuario e indique su nivel de rendimiento (Inaceptable,#Aceptable, Meritorio) y la cantidad de dinero que recibirá (2400 € multiplicado por la puntuación)
#Presentamos a la empresa
print ("Bienvenido a CORPOELEC")
#Interactuamos con el usuario
nombre = input ("¿Como se llama usted?")
print (f"Hola, {nombre}")
#Preguntamos cual fue su puntacion y declaramos la variable del salario
evaluacion = float (input ("¿Cual fue su puntacion en el evaluativo?"))
salario = 2400
#Declaramos las condiciones 
if evaluacion == 0.0:
    print (f"{nombre},usted es inaceptable en esta empresa")
    calificacion = "inaceptable"
elif evaluacion == 0.4: 
    print (f"{nombre},usted es aceptable en esta empresa,YOU'RE WELCOME ")
    calificacion = "aceptable"
elif evaluacion >= 0.6:
    print (f"{nombre},usted es meritorio para esta empresa explendorosa,YOU'RE WELCOME")
    calificacion = "meritorio"
else:
    print ("Evaluacion invalidad")
#Declaramos el procedimiento para el calculo de la cobranza para el trabajador   
cobransa = salario*evaluacion

#Para finalizar reflejamos los resultados de su cobranza
print(f"Usted estaría cobrando: {cobransa} €")