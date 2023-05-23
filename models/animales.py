import streamlit as st
class Animales:
    def __init__(self, id, nombre, tipoAnimal, edad, dieta, salud, descripcion, clasificacion, horasSueno):
        self.id = id
        self.nombre = nombre
        self.tipoAnimal = tipoAnimal
        self.edad = edad
        self.dieta = dieta
        self.salud = salud
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.horasSueno = horasSueno
        self.jugar = False

    def mostrar_info_animales(self):
        print("El", self.tipoAnimal, self.clasificacion,"llamado", self.nombre, "tiene", self.edad, "años")
        print("Tiene una condicion de salud", self.salud, ",come", self.dieta, "y duerme", self.horasSueno)
        print(self.descripcion)