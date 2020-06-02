""" El siguiente programa tiene como objetivo hacer una automatización para obtener los precios del jitomate saladette
	de manera diaria. Se usa el producto jitmate saladette pero el código es aplicable para cualquier producto de 
	cualquier página mientras se tenga registro del url de la página (línea 18), nombre de la barra de búsqueda (puede ser
	por id u otro, línea 20) y el xpath del precio del producto (línea 16).
"""
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys # Keys nos sirve para usar teclas dentro de las páginas web.
import time
import pandas as pd 
import os 
from datetime import date

# Dirección de donde tengamos el PhantomJS (Nota 1, línea 46).
path_phantom = "C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
# El xpath del precio del jitomate saladette. Se recomienda que sea xpath ya que no siempre se va a contar con un id.
xpath = "//*[@id='product_list']/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div/span[2]"
# La dirección de la página.
url = "http://lacomer.com.mx"
# Nombre de la barra de búsqueda.
nombre_id = "idSearch" # En ésta caso se buscó por id.
# Nombre del producto a buscar.
producto = "jitomate saladet"

i=0 # Contador para ir llenando el dataframe.
df = pd.DataFrame(columns = ["Fecha","Precio"]) # Creamos el dataframe con la columnas de Fecha y Precio.

while i >= 0: # Con esto hacemos que el ciclo sea infinito y el iterador vaya llenando las filas correspondientes.
	driver = webdriver.PhantomJS(path_phantom) # Hacemos que driver use el phantomJS.
	driver.get(url)  # Entramos a la página de la comercial.
	busqueda_comer = driver.find_element_by_id(nombre_id) # Buscamos la barra de búsqueda por id.
	busqueda_comer.send_keys(producto) # Escribimos en la barra de búsqueda jitomate saladet.
	busqueda_comer.send_keys(Keys.ENTER) # Damos ENTER.
	time.sleep(10)
	precio_jitomate = driver.find_elements_by_xpath(xpath) # Buscamos el precio por xpath. 
	precio="" # Nos servirá para guardar el precio ya que viene como una lista de elementos (caracteres).
	for c in precio_jitomate: 
		precio = precio + c.text
	today = str(date.today()) # Hacemos cadena de texto al día actual.
	df.loc[i]=[today,precio] # Añadimos a i-ésma fila su día y precio correspondientes.
	# Lo guardamos en la dirrección de preferencia con el nombre respectivo.
	df.to_excel(r"C:\Users\Edgar\Documents\CursosProgramacion\Phyton\Selenium\ServicioSocial\prueba7.xlsx", index = False)
	i += 1 # Incrementamos el iterador.
	driver.quit() # Cerramos el driver.
	time.sleep(3590)

""" Notas:
	1. Se necesita instalar el PhantomJS. Se anexa link: https://phantomjs.org/download.html
	2. Se necesitan los módulos: selenium (para navegar en la web), pandas (para usar bases de datos)
	y el openpyxl (para exportar bases de datos a un xlsx).
	3. Es importante que el driver.quit() esté hasta el final, ya que a lo largo del trabajo con éste código se
	llegó a al problema de que si se ponía antes de crear el xlsx, entonces había ocasiones en las que se cerraba
	y no alcanzaba a copiar todos los elementos del xpath (recordar que es una lista de caracteres). Otra solución
	al problema sería utilizar la pausa explicita (ExplicitWait) de hacer que no se cierre a menos que cargue toda
	la página. 
"""
""" Errores Comunes:
	1. No tener la versión del Chrome correspondiente con el webdriver.
	2. Que no escriba nada en el xlsx debido a lo comentado en la nota 3.
	3. Que no escirba nada en el xlsx debido a que no se implementa el for() para ir metiendo caracter por caracter.
"""