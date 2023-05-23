import requests
class Controller:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            animal = self.vista.menu_crear_animal()
            if animal:
                self.modelo.anadir_animales(animal)
        if opcion == 2:
            habitat = self.vista.menu_crear_habitat()
            if habitat:
                self.modelo.anadir_habitats(habitat)
        if opcion == 4:
            self.vista.listar_info_zoo(self.modelo.habitats,self.modelo.animales)
        if opcion == 7:
            self.vista.borrar_alimento(self.modelo.carnivoros,self.modelo.herbivoros,self.modelo.omnivoros)
        if opcion == 8:
            self.vista.llamado_api()
