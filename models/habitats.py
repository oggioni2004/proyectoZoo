import streamlit as st
class Habitats:
    def __init__(self, nombre, tipoHabitat, numeroHabitantesMAx, dieta, temperatura, clasificacion, descripcion):
        self.nombre = nombre
        self.tipoHabitat = tipoHabitat
        self.numeroHabitantesMAx = numeroHabitantesMAx
        self.dieta = dieta
        self.temperatura = temperatura
        self.clasificacion = clasificacion
        self.descripcion = descripcion

        if "animalesDeHabitat" in st.session_state:
            self.animalesDeHabitat = st.session_state["animalesDeHabitat"]
        else:
            self.animalesDeHabitat = []

    def mostrar_info_habitat(self):
        print("El", self.tipoHabitat, "puede tener como maximo", self.numeroHabitantesMAx, "animales")
        print("En este habitat comen", self.dieta, ", hay una temperatura de", self.temperatura, "y entran animales", self.clasificacion)
        print(self.descripcion)