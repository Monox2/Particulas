from particula import Particula
from algoritmos import distancia_euclidiana

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(id= 1, origen_x= 7, origen_y= 4, destino_x= 5, destino_y= 1, velocidad= 100, red= 50, green= 75, blue= 100, distancia= distancia_euclidiana)
p02 = Particula(id= 2, origen_x= 500, origen_y= 200, destino_x= 500, destino_y= 200, velocidad= 100, red= 50, green= 75, blue= 100, distancia= distancia_euclidiana)
particulas = Particulas()
particulas.agregar_final(p01)
particulas.agregar_inicio(p02)
particulas.agregar_inicio(p01)
particulas.mostrar()

