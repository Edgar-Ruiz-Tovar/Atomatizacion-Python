from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd 
import os 
from datetime import date
path_phantom = "C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
lista_productos=[
["jitomate saladete", "//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"],
["piña miel", "//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"],
["leche ultra pasteurizada lala","//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"],
["atun dolores","//*[@id='product_list']/div/div[2]/div[2]/div/div[3]/div/div[3]/div/div/span[2]"],
["frijol negro queretaro","//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"]
]

driver = webdriver.PhantomJS(path_phantom)

def url_comer(producto):
	criterio=""
	for x in producto.split(" "): 
		criterio+= "+"+x
	busqueda = ""
	for x in producto.split(" "): 
		busqueda+= "%20"+x
	url = "https://www.lacomer.com.mx/lacomer/goBusqueda.action?succId=287&ver=mislistas&succFmt=100&criterio=%s#/%s"%(criterio[1:], busqueda[3:])
	return url

class Producto():
	def __init__(self,lista):
		self.nombre=lista[0]  
		self.xpath=lista[1]

	def buscar(self):
		"""Busca el $ de un producto y lo retorna en busqueda"""
		try:
			driver.get(url_comer(self.nombre))
			driver.implicitly_wait(10)
			precio_jitomate = driver.find_elements_by_xpath(self.xpath)  
			busqueda="" 
			for c in precio_jitomate: 
				busqueda = busqueda + c.text
			return str(busqueda)
		except Exception as e: 
			return f"Error: {type(e).__name__}"
		driver.quit()

df = pd.DataFrame(columns = ["Fecha","Jitomate","Piña","Leche Lala","Atún Dolores Aceite",
"Frijol Negro Querétaro"]) # creamos el dataframe
i=0
while i<50:
	today = str(date.today()) # obtenemos la fecha 
	renglon=[today] # vaciamos el renglón al comienzo del for (sólo tendrá la fecha correspondiente)
	for producto in lista_productos:
		x=Producto(producto) # creamos el objeto x de clase Producto
		renglon.append(x.buscar()) # y le vamos añadiendo los precios de la lista_productos a renglon
	df.loc[i]=renglon # al final hacemos que reglon sea el renglón correspondiente al dataframe
	i+=1
print(df)
df.to_excel(r"C:\Users\Edgar\Documents\Actuaría\ServicioSocial\Pruebas\Prueba_1.xlsx", index = False)