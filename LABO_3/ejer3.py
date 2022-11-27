def ejercicio3():
    class animal:
        def __init__(self,sexo):
            self.sexo=sexo
        def __str__(self):
            pass
    class perro(animal):
        def sonidoanimal(self,sonido):
            print("El sonido del perro es:",sonido)
    class gato(animal):
        def sonidoanimal(self,sonido):
            print("El sonido del gato es:",sonido)
    mascota1=perro('macho')
    mascota2=gato('hembre')
    print("El sexo de la mascota 1 es: ",mascota1.sexo)
    print("El sexo de la mascota 2 es: ",mascota2.sexo)
    mascota1.sonidoanimal("guau")
    mascota2.sonidoanimal("miau")


    
            