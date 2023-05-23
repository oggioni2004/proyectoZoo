
import views.zoo as zoologicoview
import streamlit as st

if __name__ == '__main__':
    st.set_page_config(
        page_title="OggiZoo",
        page_icon="🦁",
        layout="wide"
    )
    menuZoo = zoologicoview.Zoo()
    menuZoo.mostrar_menu()

