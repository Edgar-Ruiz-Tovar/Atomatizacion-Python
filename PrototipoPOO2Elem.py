from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd 
import os 
from datetime import date
from selenium.webdriver.support import expected_conditions as EC

# Dirección del phantomJS y del sitio web de la comer
path_phantom = "C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
url = "http://lacomer.com.mx"
barra_busqueda="idSearch" # en caso de la comer sí hay id
driver = webdriver.PhantomJS(path_phantom)

# Lista de productos(nombre,xpath): lista_productos=[lista_jitomate,lista_piña_miel]
lista_productos=[
["jitomate", "//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"],
["piña miel", "//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"]
]

# Creamos la clase Producto
class Producto():
	def __init__(self,lista):
		self.nombre=lista[0]  
		self.xpath=lista[1]

	def buscar(self):
		"""Busca el $ de un producto y lo retorna en busqueda"""
		try:
			driver.get(url)
			busqueda_comer = driver.find_element_by_id(barra_busqueda)
			busqueda_comer.send_keys(self.nombre) 
			busqueda_comer.send_keys(Keys.ENTER) 
			driver.implicitly_wait(10)
			precio_jitomate = driver.find_elements_by_xpath(self.xpath)  
			busqueda="" 
			for c in precio_jitomate: 
				busqueda = busqueda + c.text
			return str(busqueda)
		except Exception as e: 
			return f"Error: {type(e).__name__}"
		driver.quit()

df = pd.DataFrame(columns = ["Fecha","Jitomate","Piña"]) # creamos el dataframe
i=0
while i<50:
	today = str(date.today()) # obtenemos la fecha 
	renglon=[today] # vaciamos el renglón al comienzo del for (sólo tendrá la fecha correspondiente)
	for producto in lista_productos:
		x=Producto(producto) # creamos el objeto x de clase Producto
		renglon.append(x.buscar()) # y le vamos añadiendo los precios de la lista_productos a renglon
	df.loc[i]=renglon # al final hacemos que reglon sea el renglón correspondiente al dataframe
	i+=1
df.to_excel(r"C:\Users\Edgar\Documents\Actuaría\ServicioSocial\Pruebas\PrototipoPOO2Elem_2.xlsx", index = False)