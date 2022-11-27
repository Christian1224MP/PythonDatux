def ejercicio7():
    import requests
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    response.json() 
    data = response.json()
    compra = data['compra']
    venta = data['venta']
    fecha_actual = data['fecha']
    print("El valor del dolar en la compra es: ",compra)
    print("El valor del dolar en la venta es: ",venta)
    print("La fecha del cambio actual del dolara es: ",fecha_actual)
    print("Fin de ejecucion")

