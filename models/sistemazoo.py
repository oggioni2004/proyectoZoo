import streamlit as st
class Sistema:
    #clase sistema se encarga de llevar las clases animales y habitats, es el modelo principal donde se añaden los metodos
    def __init__(self):
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales=[]

        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []

        if "carnivoros" in st.session_state:
            self.carnivoros = st.session_state["carnivoros"]
        else:
            self.carnivoros = ["carne","pescado","pollo"]

        if "herbivoros" in st.session_state:
            self.herbivoros = st.session_state["herbivoros"]
        else:
            self.herbivoros = ["plantas","hierbas","algas"]

        if "omnivoros" in st.session_state:
            self.omnivoros = st.session_state["omnivoros"]
        else:
            self.omnivoros = ["carne","pescado","pollo","plantas","hierbas","algas"]

    def anadir_animales(self, animal):                  #añade animales
        self.animales.append(animal)
        st.session_state["animales"] = self.animales

    def anadir_habitats(self, habitat):                 #añade habitats
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats

    #actualiza la info de los habitats
    def actualizar_habitats(self, nombre, tipoHabitat = None, numeroHabitantesMAx = None, dieta = None, temperatura = None, clasificacion = None, descripcion = None):
        for habitat in self.habitats:
            if habitat.nombre == nombre:
                if tipoHabitat:
                    habitat.tipoHabitat = tipoHabitat
                if numeroHabitantesMAx:
                    habitat.numeroHabitantesMAx = numeroHabitantesMAx
                if dieta:
                    habitat.dieta = dieta
                if temperatura:
                    habitat.temperatura = temperatura
                if clasificacion:
                    habitat.clasificacion = clasificacion
                if descripcion:
                    habitat.descripcion = descripcion

    #actualiza la info de los animales si se requiere
    def actualizar_animales(self, id, nombre = None, tipoAnimal = None, edad = None, dieta = None, salud = None, descripcion = None, clasificacion = None, horasSueno = None):
        for animal in self.animales:
            if animal.id == id:
                if nombre:
                    animal.nombre = nombre
                if tipoAnimal:
                    animal.tipoAnimal = tipoAnimal
                if edad:
                    animal.edad = edad
                if dieta:
                    animal.dieta = dieta
                if salud:
                    animal.salud = salud
                if descripcion:
                    animal.descripcion = descripcion
                if clasificacion:
                    animal.clasificacion = clasificacion
                if horasSueno:
                    animal.horasSueno = horasSueno

    def borrar_alimento_lista(self,tipo=None, borrar=None):    #borra los alimentos que hay segun su tipo
        tipo1 = tipo
        if tipo1 == "carnivoros":
            for i in range(len(self.carnivoros)):
                if str(i) == borrar:
                    self.carnivoros.pop(int(i))
        if tipo1 == "herbivoros":
            for i in range(len(self.herbivoros)):
                if str(i) == borrar:
                    self.herbivoros.pop(int(i))
        if tipo1 == "omnivoros":
            for i in range(len(self.omnivoros)):
                if str(i) == borrar:
                    self.omnivoros.pop(int(i))

