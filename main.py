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