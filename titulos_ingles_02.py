
import requests, pandas, sys, os.path;

carpeta = 'c:\\Springer\\'
archivo_excel = carpeta + 'titulos_ingles_02.xlsx'
comodines = '/'+'\\'+'*:?"|<>'

df = pandas.read_excel(archivo_excel, skiprows=0)
for index, linea in df.iterrows():
	url_pdf = linea ['Enlace']
	nombre_pdf = linea ['Titulo']
	for caracter in comodines:
		nombre_pdf = nombre_pdf.replace ( caracter, '_' )
	nombre_pdf = carpeta + nombre_pdf
	print(nombre_pdf)
	if os.path.isfile(nombre_pdf):
		continue;
	pdf = open(nombre_pdf, "wb")
	r = requests.get(url_pdf, stream = True)
	total_length = r.headers.get('content-length')
	if total_length is None:
		pdf.write(r.content)
		pdf.close()
	else:
		dl = 0
		total_length = int(total_length)
		for data in r.iter_content(chunk_size=4096):
			pdf.write(data)
		pdf.close()
