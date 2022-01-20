from os import system
system("cls")

nom=input("Ingresa el nombre del archivo .txt: ")
system("cls")
abre=open(nom+".txt","a")

cant=int(input("Ingresa la cantidad de equipos participantes: "))
cant_save=cant
guarda=[]
ruedas=int(input("Ingresa la cantidad de veces que un equipo se va a enfrentar con cada uno de los otros: "))

system("cls")
print(nom)
print()
for r in range(1,ruedas+1):
	extra_impar=0
	extra_par=0
	if cant%2!=0:
		cant=cant+1
	for fechas in range(1,cant-1+1):
		if r!=1 or fechas!=1:
			print()
		print("FECHA",fechas+(r-1)*(cant-1))
		if r!=1 or fechas!=1:
			abre.write("\n")
		abre.write("FECHA "+str(fechas+(r-1)*(cant-1))+"\n")
		if fechas%2!=0:
			extra_impar +=1
			loc=extra_impar+1
			vis=cant+extra_impar-2
			for partidos in range(1,int(cant/2+1)):
				if partidos==1:
					if cant_save%2==0:
						guarda.append(extra_impar)
						guarda.append(cant)
						print(guarda[abs(r%2-1)], guarda[r%2])
						abre.write(str((guarda[abs(r%2-1)]))+" vs ")
						abre.write(str(guarda[r%2])+"\n")
						guarda.remove(extra_impar)
						guarda.remove(cant)
					else:					
						print("EQUIPO LIBRE", extra_impar)
						abre.write("EQUIPO LIBRE"+" vs ")
						abre.write(str(extra_impar)+"\n")
				else:
					if loc >= cant:
						loc = loc+cant-1
					if vis >= cant:
						vis = vis-cant+1
					if vis <1:
						vis = vis+cant-1
					guarda.append(loc)
					guarda.append(vis)						
					print(guarda[abs(r%2-1)], guarda[r%2])
					abre.write(str((guarda[abs(r%2-1)]))+" vs ")
					abre.write(str(guarda[r%2])+"\n")
					guarda.remove(loc)
					guarda.remove(vis)					
					loc +=1
					vis -=1
		else:
			extra_par +=1
			loc=(int(cant/2+extra_par+1))
			vis=(int(cant/2+extra_par-1))
			for partidos in range(1,int(cant/2+1)):
				if partidos==1:
					if cant_save%2==0:
						guarda.append(cant)
						guarda.append(int(cant/2+extra_par))					
						print(guarda[abs(r%2-1)], guarda[r%2])
						abre.write(str((guarda[abs(r%2-1)]))+" vs ")
						abre.write(str(guarda[r%2])+"\n")
						guarda.remove(cant)
						guarda.remove(int(cant/2+extra_par))
					else:
						print("EQUIPO LIBRE",(int(cant/2+extra_par)))
						abre.write("EQUIPO LIBRE"+" vs ")
						abre.write(str(int(cant/2+extra_par))+"\n")
				else:
					if loc >= cant:
						loc = loc-cant+1
					if vis < 1:
						vis = vis+cant-1
					guarda.append(loc)
					guarda.append(vis)						
					print(guarda[abs(r%2-1)], guarda[r%2])
					abre.write(str((guarda[abs(r%2-1)]))+" vs ")
					abre.write(str(guarda[r%2])+"\n")
					guarda.remove(loc)
					guarda.remove(vis)
					loc +=1
					vis -=1