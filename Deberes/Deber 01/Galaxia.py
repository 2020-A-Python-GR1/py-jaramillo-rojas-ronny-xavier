import os
class Galaxia:
	def __init__(self, nombre, anio_des, distancia, grupo, tipo):
		self.nombre = nombre
		self.anio_des = anio_des
		self.distancia = distancia
		self.grupo = grupo
		self.tipo = tipo
	def add_galaxy(obj):
		try:
			path = "./"+obj.nombre+".txt"
			galaxy_file = open(path,'a')
			galaxy_file.writelines(["Nombre de Galaxia:"+obj.nombre+"\n","Año de Descubrimiento:"+str(obj.anio_des)+"\n","Distancia desde la Tierra:"+str(obj.distancia)+"\n","Pertenece al Grupo Local de Galaxias:"+str(obj.grupo)+"\n","Tipo:"+obj.tipo+"\n"])
			galaxy_file.close()					
		except Exception as Error:
			print("Error al añadir galaxia, verifique que haya ingresado caracteres válidos.")
	def modify_galaxy(opcion, nuevoValor, obj):
		try:
			path = "./"+obj.nombre+".txt"
			#galaxy_file = open(path,'w')
			def modify_name():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Nombre de Galaxia:"+str(obj.nombre), "Nombre de Galaxia:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
				os.rename(str(obj.nombre)+".txt",str(nuevoValor)+".txt")
			def modify_anio():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Año de Descubrimiento:"+str(obj.anio_des), "Año de Descubrimiento:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_dist():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Distancia desde la Tierra:"+str(obj.distancia), "Distancia desde la Tierra:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_grupo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Pertenece al Grupo Local de Galaxias:"+str(obj.grupo), "Pertenece al Grupo Local de Galaxias:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_tipo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Tipo:"+str(obj.tipo), "Tipo:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modificar():
				opciones = {
					"1":modify_name,
					"2":modify_anio,
					"3":modify_dist,
					"4":modify_grupo,
					"5":modify_tipo
				}
				return opciones[opcion]()
			return modificar()		
		except Exception as Error:
			print("Error al modificar galaxia."+Error)
			return None
	def get_galaxy(nombre):
		try:
			path = "./"+nombre+".txt"
			galaxy_file = open(path)
			info_galaxia=galaxy_file.read().splitlines()
			galaxy_file.close()
			#return info_galaxia
			return Galaxia(info_galaxia[0].split(":")[1],info_galaxia[1].split(":")[1],info_galaxia[2].split(":")[1],info_galaxia[3].split(":")[1],info_galaxia[4].split(":")[1])
		except Exception as Error:
			return None
	def get_galaxy_info(nombre):
		try:
			path = "./"+nombre+".txt"
			galaxy_file = open(path)
			info_galaxia=galaxy_file.read().splitlines()
			galaxy_file.close()
			return info_galaxia
		except Exception as Error:
			return None		
	def remove_galaxy(nombre):
		try:
			path = "./"+nombre+".txt"
			os.remove(path)
			return True
		except Exception as Error:
			return False
class Cuerpos:
	def __init__(self, galaxia_padre, nombre_cuerpo, tipo_cuerpo, tamanio, color, masa):
		self.galaxia_padre = galaxia_padre
		self.nombre_cuerpo = nombre_cuerpo
		self.tipo_cuerpo = tipo_cuerpo
		self.tamanio = tamanio
		self.color = color
		self.masa = masa
	def add_body(obj):
		try:
			path = "./"+obj.galaxia_padre+".txt"
			galaxy_file = open(path,'a')
			galaxy_file.writelines(["Nombre del Cuerpo:"+obj.nombre_cuerpo+"\n","Tipo de Cuerpo:"+obj.tipo_cuerpo+"\n","Tamaño:"+str(obj.tamanio)+"\n","Color:"+obj.color+"\n","Masa:"+str(obj.masa)+"\n"])
			galaxy_file.close()
		except Exception as Error:
			print("Error al añadir cuerpo.")
	def modify_body(opcion, nuevoValor, obj):
		try:
			path = "./"+obj.galaxia_padre+".txt"
			#galaxy_file = open(path,'w')
			def modify_name_cuerpo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				for line in galaxy_file:
  					stripped_line = line.strip()
  					new_line = stripped_line.replace("Nombre del Cuerpo:"+str(obj.nombre_cuerpo), "Nombre del Cuerpo:"+str(nuevoValor))
  					new_file_content += new_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_tipo_cuerpo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				entro=False
				for line in galaxy_file:
					stripped_line = line.strip()
					if stripped_line=="Nombre del Cuerpo:"+str(obj.nombre_cuerpo):
						entro = True
					if "Tipo de Cuerpo:" in stripped_line and entro:
						entro=False
						new_line = stripped_line.replace("Tipo de Cuerpo:"+str(obj.tipo_cuerpo), "Tipo de Cuerpo:"+str(nuevoValor))
						new_file_content += new_line +"\n"
					else:
						new_file_content += stripped_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_tamanio_cuerpo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				entro=False
				for line in galaxy_file:
					stripped_line = line.strip()
					if stripped_line=="Nombre del Cuerpo:"+str(obj.nombre_cuerpo):
						entro = True
					if "Tamaño:" in stripped_line and entro:
						entro=False
						new_line = stripped_line.replace("Tamaño:"+str(obj.tamanio), "Tamaño:"+str(nuevoValor))
						new_file_content += new_line +"\n"
					else:
						new_file_content += stripped_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_color_cuerpo():
				galaxy_file = open(path, "r")
				new_file_content = ""
				entro=False
				for line in galaxy_file:
					stripped_line = line.strip()
					if stripped_line=="Nombre del Cuerpo:"+str(obj.nombre_cuerpo):
						entro = True
					if "Color:" in stripped_line and entro:
						entro=False
						new_line = stripped_line.replace("Color:"+str(obj.color), "Color:"+str(nuevoValor))
						new_file_content += new_line +"\n"
					else:
						new_file_content += stripped_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modify_masa():
				galaxy_file = open(path, "r")
				new_file_content = ""
				entro=False
				for line in galaxy_file:
					stripped_line = line.strip()
					if stripped_line=="Nombre del Cuerpo:"+str(obj.nombre_cuerpo):
						entro = True
					if "Masa:" in stripped_line and entro:
						entro=False
						new_line = stripped_line.replace("Masa:"+str(obj.masa), "Masa:"+str(nuevoValor))
						new_file_content += new_line +"\n"
					else:
						new_file_content += stripped_line +"\n"
				galaxy_file.close()
				galaxy_file = open(path, "w")
				galaxy_file.write(new_file_content)
				galaxy_file.close()
			def modificar_cuerpo():
				opciones = {
					"1":modify_name_cuerpo,
					"2":modify_tipo_cuerpo,
					"3":modify_tamanio_cuerpo,
					"4":modify_color_cuerpo,
					"5":modify_masa
				}
				return opciones[opcion]()
			return modificar_cuerpo()
		except Exception as Error:
			print("Error al modificar el cuerpo."+Error)
			return None
	def get_body(nombre_galaxy,nombre_cuerpo):
		try:
			path = "./"+str(nombre_galaxy)+".txt"
			galaxy_file = open(path)
			info_galaxia=galaxy_file.read().splitlines()
			info_body = []
			x = 0
			for line in info_galaxia:
				if line==("Nombre del Cuerpo:"+str(nombre_cuerpo)):
					i=0
					while(i<=4):
							info_body.append(info_galaxia[x].split(":")[1])
							x+=1
							i+=1
				x+=1			
			galaxy_file.close()
			if info_body:
				return Cuerpos(nombre_galaxy,info_body[0],info_body[1],info_body[2],info_body[3],info_body[4])
			else:
				return None
		except Exception as Error:
			print("Cuerpo no encontrado."+Error)
			return None
	def del_body(nombre_galaxy,nom_body):
		try:
			path = "./"+str(nombre_galaxy)+".txt"
			galaxy_file = open(path,"r")
			lines = galaxy_file.readlines()
			galaxy_file.close()
			galaxy_file = open(path, "w")
			entro = False
			for line in lines:
				if line.strip("\n") == "Nombre del Cuerpo:"+str(nom_body.nombre_cuerpo):		
					entro = True		
				if entro != True:
					galaxy_file.write(line)
				if entro:
					if line.strip("\n") == "Masa:"+str(nom_body.masa):
						entro = False
			galaxy_file.close()
			return True
		except Exception as Error:
			print("Error en la eliminación del cuerpo"+Error)
			return False
	
	
	
	
while(True):
	print("Bienvenido a Galaxy Note, por favor, ingrese el tipo de operación que desea realizar:\n")
	print("1 - Agregar una Galaxia\n2 - Ver una Galaxia y sus Cuerpos\n3 - Modificar una Galaxia o sus Cuerpos\n4 - Eliminar una Galaxia o un Cuerpo de una Galaxia\n5 - Salir del programa")
	inicio = input()
	if(inicio=="1"):
		print("Por favor, ingrese los siguientes datos:\nNombre de la Galaxia:")
		nombre = input()
		print("Año de Descubrimiento (Integer):")
		anio = input()
		print ("Distancia desde la Tierra (Decimal - Año Luz):")
		dist = input()
		print ("Pertenece al Grupo Local de Galaxias:\n1 -> Sí\n2 -> No")
		if(input()=="1"):
			pert = True
		else:
			pert = False
		print("Tipo de Galaxia (Forma):")
		tipo=input()
		lista_cuerpos = []
		#print("Galaxia añadida con éxito!")
		while(True):
			print("Por favor, ingrese 1 si desea agregar un cuerpo celeste a esta galaxia o 2 para regresar al menú")
			createbody = input()
			if(createbody!="2"):
				print("Por favor, ingrese los siguientes datos:\nNombre del Cuerpo:")
				nombre_cuerpo = input()
				print("Tipo de Objeto:")
				tipo_cuerpo = input()
				print("Tamaño (Decimal):")
				tamanio = input()
				print("Color:")
				color = input()
				print("Masa (Decimal):")
				masa = input()
				nuevo = Cuerpos(nombre,nombre_cuerpo,tipo_cuerpo,tamanio,color,masa)
				lista_cuerpos.append(nuevo)
			else:
				Galaxia.add_galaxy(Galaxia(nombre,anio,dist,pert,tipo))
				if lista_cuerpos:
					for cuerpo in lista_cuerpos:
						Cuerpos.add_body(cuerpo)
				break
	elif(inicio=="2"):
		while(True):
			print("Por favor, ingrese el nombre de la galaxia que quiere ver o 2 para regresar al menú")
			vergalaxy = input()
			if(vergalaxy!="2"):
				buscada = Galaxia.get_galaxy(vergalaxy)
				if(buscada != None):
					while(True):
						print("Por favor, ingrese una de las siguientes opciones:")
						print("1 - Ver la información de la Galaxia\n2 - Ver la información de la Galaxia y todos sus cuerpos\n3 - Ver la información de un cuerpo específico\n4 - Regresar")
						tipo_search = input()
						if (tipo_search=="1"):
							print("Nombre de Galaxia:"+str(buscada.nombre)+"\nAño de Descubrimiento:"+str(buscada.anio_des)+"\nDistancia desde la Tierra:"+str(buscada.distancia)+"\nPertenece al Grupo Local de Galaxias:"+str(buscada.grupo)+"\nTipo:"+str(buscada.tipo))
						if (tipo_search=="2"):
							vergalaxy_info = Galaxia.get_galaxy_info(vergalaxy)
							for linea in vergalaxy_info:
								print(str(linea)+"\n")
						if (tipo_search=="3"):
							print("Ingrese el nombre del cuerpo del que desea ver la información.")
							body_opt = input()
							body_info = Cuerpos.get_body(buscada.nombre,body_opt)
							if body_info != None:
								print("Nombre del Cuerpo:"+str(body_info.nombre_cuerpo)+"\nTipo de Cuerpo:"+str(body_info.tipo_cuerpo)+"\nTamaño del Cuerpo:"+str(body_info.tamanio)+"\nColor:"+str(body_info.color)+"\nMasa del Cuerpo:"+str(body_info.masa))
							else:
								print("No existe el cuerpo especificado dentro de esta galaxia.")
						if (tipo_search=="4"):
							break
				else:
					print("No existe la galaxia especificada.")
			elif(vergalaxy=="2"):
				break
	elif(inicio=="3"):
		while(True):
			print("Por favor, ingrese el nombre de la galaxia de la cual modificará los datos o cuerpos, ingrese 2 para regresar al menú.")
			modifygalaxy = input()
			if (modifygalaxy!="2"):
				modificada = Galaxia.get_galaxy(modifygalaxy)
				if(modificada != None):
					while(True):
						print("Por favor, ingrese el número del parámetro que quiere modificar.")
						print("1 - Nombre\n2 - Año de Descubrimiento\n3 - Distancia desde la Tierra\n4 - Pertenencia al Grupo Local de Galaxias\n5 - Tipo de Galaxia (Forma)\n6 - Agregar un Cuerpo Celeste\n7 - Modificar un Cuerpo Celeste Existente\n8 - Regresar")
						tipo_modificacion = input()
						if(tipo_modificacion=="1"):
							print("Por favor, ingrese el nuevo nombre de la Galaxia:")
							nuevo = input()
							Galaxia.modify_galaxy(str(tipo_modificacion),str(nuevo),modificada)
							print("Nombre modificado con éxito!")
							break
						elif(tipo_modificacion=="2"):
							print("Por favor, ingrese el nuevo año de descubrimiento de la Galaxia:")
							nuevo = input()
							Galaxia.modify_galaxy(str(tipo_modificacion),str(nuevo),modificada)
							print("Año modificado con éxito!")
							break
						elif(tipo_modificacion=="3"):
							print("Por favor, ingrese la nueva distancia desde la tierra de la Galaxia:")
							nuevo = input()
							Galaxia.modify_galaxy(str(tipo_modificacion),str(nuevo),modificada)
							print("Distancia modificada con éxito!")
							break
						elif(tipo_modificacion=="4"):
							print("Por favor, ingrese si pertenece al grupo local de galaxias:\n1 -> Sí\n2 -> No:")
							nuevo = input()
							if(nuevo=="1"):
								nuevo = True
							elif(nuevo=="2"):
								nuevo = False
							Galaxia.modify_galaxy(str(tipo_modificacion),nuevo,modificada)
							print("Parámetro modificado con éxito!")
							break
						elif(tipo_modificacion=="5"):
							print("Por favor, ingrese el nuevo tipo de la Galaxia:")
							nuevo = input()
							Galaxia.modify_galaxy(str(tipo_modificacion),str(nuevo),modificada)
							print("Tipo modificado con éxito!")
							break
						elif(tipo_modificacion=="6"):
							print("Por favor, ingrese los siguientes datos:\nNombre del Cuerpo:")
							nombre_cuerpo = input()
							print("Tipo de Objeto:")
							tipo_cuerpo = input()
							print("Tamaño (Decimal):")
							tamanio = input()
							print("Color:")
							color = input()
							print("Masa (Decimal):")
							masa = input()
							nuevo = Cuerpos(modifygalaxy,nombre_cuerpo,tipo_cuerpo,tamanio,color,masa)
							Cuerpos.add_body(nuevo)
							print("Cuerpo agregado exitosamente!")
							break
						elif(tipo_modificacion=="7"):
							while (True):
								print("Por favor, ingrese el nombre del Cuerpo Celeste que desea modificar o 2 para regresar al menú:")
								nuevo = input()
								if(nuevo!="2"):								
									bodify = Cuerpos.get_body(str(modificada.nombre),nuevo)
									if bodify!=None:
										print("Por favor, ingrese el número del parámetro que desea modificar.")
										print("1 - Nombre del Cuerpo\n2 - Tipo de Objeto\n3 - Tamaño\n4 - Color\n5 - Masa\n6 - Regresar")
										option = input()
										if(option=="1"):
											print("Por favor, ingrese el nuevo nombre del Cuerpo Celeste.")
											nuevoValor = input()
											Cuerpos.modify_body(option,nuevoValor,bodify)
											print("Nombre cambiado con éxito!")
										elif(option=="2"):
											print("Por favor, ingrese el nuevo tipo de objeto a desginar al cuerpo.")
											nuevoValor = input()
											Cuerpos.modify_body(option,nuevoValor,bodify)
											print("Tipo cambiado con éxito!")
										elif(option=="3"):
											print("Por favor, ingrese el nuevo tamaño del Cuerpo Celeste.")
											nuevoValor = input()
											Cuerpos.modify_body(option,nuevoValor,bodify)
											print("Tamaño cambiado con éxito")
										elif(option=="4"):
											print("Por favor, ingrese el nuevo color del Cuerpo Celeste.")
											nuevoValor = input()
											Cuerpos.modify_body(option,nuevoValor,bodify)
											print("Color cambiado con éxito!")
										elif(option=="5"):
											print("Por favor, ingrese la nueva masa del Cuerpo Celeste.")
											nuevoValor = input()
											Cuerpos.modify_body(option,nuevoValor,bodify)
											print("Masa cambiada con éxito!")
										elif(option=="6"):
											break
									else:
										print("El cuerpo especificado no existe.")
								else:
									break
						elif(tipo_modificacion=="8"):
							break
						else:
							print("Ingrese una opción válida.")
					
	
				else:
					print("No existe la galaxia especificada.")
			else:
				break
	elif(inicio=="4"):
		while(True):
			print("Por favor, ingrese el número de opción que desea ejecutar.")
			print("1 - Eliminar una Galaxia\n2 - Eliminar un Cuerpo Celeste de una Galaxia\n3 - Regresar")
			delopt = input()
			if(delopt=="1"):
				print("Por favor, ingrese el nombre de la galaxia que desea eliminar.")
				delgal = input()
				done = Galaxia.remove_galaxy(delgal)
				if(done):
					print("La galaxia y todos sus cuerpos han sido removidos exitosamente!")
				else:
					print("La galaxia especificada no existe.")
			if(delopt=="2"):
				print("Por favor, ingrese el nombre de la galaxia donde se halla el cuerpo que desea eliminar")
				galnom = input()
				galfromdel = Galaxia.get_galaxy(galnom)
				if(galfromdel!=None):
					print("Por favor, ingrese el nombre del cuerpo que desea eliminar de la galaxia")
					bodnom = input()
					bodfromdel = Cuerpos.get_body(galfromdel.nombre,bodnom)
					if bodfromdel != None:
						res = Cuerpos.del_body(galfromdel.nombre,bodfromdel)
						if(res):
							print("Cuerpo eliminado con éxito!")
						else:
							print("Error en la eliminación del cuerpo.")
					else:
						print("El Cuerpo Celeste especificado no existe!")
				else:
					print("La galaxia especificada no existe!")
			if(delopt=="3"):
				break
	elif(inicio=="5"):
		exit()
