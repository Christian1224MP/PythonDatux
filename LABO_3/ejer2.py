def ejercicio2():
    class catalogo:
        productos=[]
        def __init__(self,productos=[]) :
            self.productos=productos
        def agregar(self,prod):
            self.productos.append(prod)
        def mostrar(self):
            for prod in self.productos:
                print(prod)            
    class producto:
        def __init__(self,nombre,cantidad):
            self.nombre=nombre
            self.cantidad=cantidad
            print('Se ha creado el producto:', self.nombre)
        def __str__(self):
            return ''.format() 
    #CREAMOS ALGUNOS PRODUCTOS PARA NUESTRO CATALOGO
    prod=producto("gloria",20)   
    c=catalogo([prod])
    c.mostrar()
    c.agregar(producto("nescafe",15))
    c.mostrar()


