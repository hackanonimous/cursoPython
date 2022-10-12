## for es una estructura de ciclo
## que nos permite iterar elementos o varibales
# for numero in range(1,11):
#   print(numero)

##while tambien es una estructura de ciclo
##int es un metododo de python que transforma un dato
## tipo texto a un dato de tipo numerico real o entero
## input es un metodo de python que pide un dato
## por consola al usuario
condicion=True
while condicion==True:
  numero=int(input('ingresa el numero ganador:'))
  if numero==10:
    print('ganaste el premio')
    condicion=False
  else:
    print('sientate chato ese no es el numero')

##CREAR UN PROGRAMA QUE ME PIDA MI EDAD
##SI INGRESO UNA EDAD INCORRECTA EL PROGRAMA
##SEGUIRA PIDIENDO MI EDAD
##SI ES LA EDAD CORRECTA ME MOSTRARA UN MENSAJE DE CORRECTO
##Y SE TERMINARA LA EJECUCION
password='70133573'
condicion=True
intentos=1
while condicion==True:
	print('este es tu',intentos,' intentos')
	newPassword=input('ingresa el password correcto:')
	if newPassword==password:
		print('binevenido al sistema joven ilustre')
		condicion=False
	else:
		print('eres un gil')
		intentos+=1


## AVERIGUAR SOBRE FUNCIONES