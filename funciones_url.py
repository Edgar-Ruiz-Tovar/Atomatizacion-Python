def url_comer(producto):
	criterio=""
	for x in producto.split(" "): 
		criterio+= "+"+x
	busqueda = ""
	for x in producto.split(" "): 
		busqueda+= "%20"+x
	url = "https://www.lacomer.com.mx/lacomer/goBusqueda.action?succId=287&ver=mislistas&succFmt=100&criterio=%s#/%s"%(criterio[1:], busqueda[3:])
	return url

def url_chedrahui(producto):
	busqueda=""
	for x in producto.split(" "):
		x=x.replace('ñ','%C3%B1')
		busqueda+="%20"+x
	url = "https://www.chedraui.com.mx/search?text=%s&method=enter"%(busqueda[3:])
	return url	


def url_walmart(producto):
	busqueda = ""
	for x in producto.split(" "):
		busqueda+= "%20"+x
	url= "https://super.walmart.com.mx/productos?Ntt=%s"%(busqueda[3:])
	return url