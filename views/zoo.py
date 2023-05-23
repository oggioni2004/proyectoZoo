import models.animales as animalModel
import models.habitats as habitatModel
import models.sistemazoo as sistemaZoo
import controllers.controllerszoo as controllerZoo
import streamlit as st
import requests

class Zoo:
    def mostrar_menu(self):
        sistema = sistemaZoo.Sistema()
        controlador = controllerZoo.Controller(sistema, self)
        st.title("🐾:orange[Bienvenido a el Zoo]👋")
        st.divider()

        st.sidebar.caption("1️⃣ Añadir info del animal🐯")
        opcion1 = st.sidebar.button(":blue[Click aqui]",1)
        st.sidebar.divider()

        st.sidebar.caption("2️⃣ Crear habitat🏞️")
        opcion2 = st.sidebar.button(":blue[Click aqui]",2)
        st.sidebar.divider()

        st.sidebar.caption("3️⃣ Asignar animal a habitat✅")
        opcion3 = st.sidebar.button(":blue[Click aqui]",3)
        st.sidebar.divider()

        st.sidebar.caption("4️⃣ Listar info Zoo🧩")
        opcion4 = st.sidebar.button(":blue[Click aqui]",4)
        st.sidebar.divider()

        st.sidebar.caption("5️⃣ Acciones animales🙈🙉🙊")
        opcion5 = st.sidebar.button(":blue[Click aqui]",5)
        st.sidebar.divider()

        st.sidebar.caption("6️⃣ Agregar comidas🍖")
        opcion6 = st.sidebar.button(":blue[Click aqui]",6)
        st.sidebar.divider()

        st.sidebar.caption("7️⃣ Quitar comidas❌")
        opcion7 = st.sidebar.button(":blue[Click aqui]",7)
        st.sidebar.divider()

        st.sidebar.caption("8️⃣ Pagina web🗺️")
        opcion8 = st.sidebar.button(":blue[Click aqui]", 8)
        st.sidebar.divider()

        if opcion1:
            st.session_state["opcion"]=1
        elif opcion2:
            st.session_state["opcion"]=2
        elif opcion3:
            st.session_state["opcion"]=3
        elif opcion4:
            st.session_state["opcion"]=4
        elif opcion5:
            st.session_state["opcion"]=5
        elif opcion6:
            st.session_state["opcion"]=6
        elif opcion7:
            st.session_state["opcion"]=7
        elif opcion8:
            st.session_state["opcion"]=8

        if "opcion" in st.session_state:
            controlador.ejecutar_opcion(st.session_state["opcion"])

    def menu_crear_animal(self):
        with st.expander("Formulario animales"):
            st.subheader("Escribe los datos del animal que se agregara 😎")
            id = st.text_input("Ingrese el id del animal: ")
            st.divider()
            nombre = st.text_input("Ingrese el nombre del animal: ")
            st.divider()
            tipoAnimal = st.text_input("Ingrese el tipo de animal: ")
            st.divider()
            edad = st.slider("Ingrese la edad del animal: ",0,50,25)
            st.write("El animal tiene", edad, "años")
            st.divider()
            dieta = st.selectbox("Escoja la dieta del animal: ", ("carnivoros","herbivoros","omnivoros"))
            st.divider()
            salud = st.selectbox("Condiciones del animal: ", ("buena","regular","mala"))
            st.divider()
            descripcion = st.text_input("Describa el animal: ")
            st.divider()
            clasificacion = st.selectbox("Clasificacion del animal: ",("terrestres","acuatico","aereo"))
            st.divider()
            horasSueno = st.slider("Cuanto debe dormir el animal: ",0,24,12)
            st.write("El animal tiene que dormir", horasSueno, "horas")
            st.divider()
            botom_crear = st.button("Ingresar datos")

        if botom_crear:
            nuevoAnimal = animalModel.Animales(id,nombre,tipoAnimal,edad,dieta,salud,descripcion,clasificacion,horasSueno)
            st.success("Se ha guardado correctamente el animal")
            return nuevoAnimal

    def menu_crear_habitat(self):
        with st.expander("Formulario habitat"):
            nombre = st.text_input("Ingrese el codigo o el nombre del habitat: ")
            st.divider()
            tipoHabitat = st.selectbox("Escoja el tipo de habitat: ", ("desertico","selvatico","polar","acuatico"))
            st.divider()
            numeroHabitantesMAx = st.slider("numero habitantes ", 0,50,25)
            st.divider()
            dieta = st.selectbox("Escoja la dieta del habitat: ", ("carnivoros", "herbivoros", "omnivoros"))
            st.divider()
            temperatura = st.slider("Escoja una temperatura: ",-40,40,0)
            st.divider()
            clasificacion = st.selectbox("Clasificacion del habitat: ", ("terrestres", "acuatico", "aereo"))
            st.divider()
            descripcion = st.text_input("Describa el habitat: ")
            st.divider()
            botom_habitat = st.button("Ingresar datos")

        if botom_habitat:
            nuevoHabitat = habitatModel.Habitats(nombre,tipoHabitat,numeroHabitantesMAx,dieta,temperatura,clasificacion,descripcion)
            st.success("Se ha creado correctamente el habitat")
            return nuevoHabitat

    def listar_info_zoo(self,habitats,animales):
        if len(habitats)==0:
            st.error("No hay info en el zoo")
        else:
            st.subheader("Lista info del zoo")
            for habitat in habitats:
                st.subheader("Info habitats: ")
                st.write("EL Nombre del habitat es: ", habitat.nombre)
                st.write("El tipo del habitat es: ", habitat.tipoHabitat)
                st.divider()

            for animal in animales:
                st.subheader("Info animales: ")
                st.write("EL Nombre del habitat es: ", animal.nombre)
                st.write("El Id es: ", animal.id)

    def borrar_alimento(self,carnivoro,herbivoros,omnivoros):
        eleccion1 = st.selectbox("Escoje entre: ",("carnivoros", "herbivoros", "omnivoros"))
        i=0
        if eleccion1 == "carnivoros":
            for car in carnivoro:
                st.write(i,") Alimento :", car)
                i+=1
            borrar_alimento = st.text_input("Escriba el numero del alimento carnivoro: ")


        elif eleccion1 == "herbivoros":
            for her in herbivoros:
                st.write(i,") Alimento :", her)
                i+=1
            borrar_alimento = st.text_input("Escriba el numero del alimento herbivoro: ")

        elif eleccion1 == "omnivoros":
            for omn in omnivoros:
                st.write(i,") Alimento :", omn)
                i+=1
            borrar_alimento = st.text_input("Escriba el numero del alimento omnivoro: ")


        seguir = st.button("seguir")

        if seguir:
            sistemaZoo.Sistema.borrar_alimento_lista("",eleccion1,borrar_alimento)
            st.success("Se ha borrado")



    def solicitar_info_animal(self, datoAnimal):
        return input(datoAnimal)

    def solicitar_info_habitat(self, datoHabitat):
        return input(datoHabitat)

    def llamado_api(self):
        llamado = requests.get("https://swapi.dev/api/people/1/")
        datos = llamado.json()
        st.write("Los datos que hay son: ")
        for llave, valor in datos.items():
            st.write(llave, ":", valor)

