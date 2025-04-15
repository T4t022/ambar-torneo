
import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.set_page_config(page_title="Diseñador de Camisetas – Ámbar", layout="wide")

st.image("ambar-logo-for-light.png", width=150)
st.title("Diseñador de Camisetas para el Torneo de la Construcción")
st.markdown("Personalizá tu camiseta con más detalles y visualizala sobre una silueta real.")

# Cargar silueta base
silueta = Image.open("silueta-camiseta.png").convert("RGBA")

# Configuraciones de estilo
st.sidebar.header("🎨 Personalización de Camiseta")

color_base = st.sidebar.color_picker("Color base", "#1E90FF")
color_mangas = st.sidebar.color_picker("Color de mangas", "#FFFFFF")
color_cuello = st.sidebar.color_picker("Color del cuello", "#FFD700")
estilo = st.sidebar.selectbox("Estilo de diseño", ["Liso", "Franjas", "Banda diagonal", "Bloques"])
mostrar = st.sidebar.button("Mostrar camiseta")

if mostrar:
    # Crear nueva imagen sobre silueta
    camiseta = silueta.copy()
    draw = ImageDraw.Draw(camiseta)

    # Área de torso para diseño (simplificada)
    torso_area = (80, 80, 220, 320)
    if estilo == "Liso":
        draw.rectangle(torso_area, fill=color_base)
    elif estilo == "Franjas":
        for i in range(torso_area[0], torso_area[2], 20):
            draw.rectangle([i, torso_area[1], i+10, torso_area[3]], fill=color_base)
            draw.rectangle([i+10, torso_area[1], i+20, torso_area[3]], fill=color_mangas)
    elif estilo == "Banda diagonal":
        draw.polygon([(80, 320), (220, 80), (220, 320)], fill=color_base)
    elif estilo == "Bloques":
        draw.rectangle([80, 80, 150, 200], fill=color_base)
        draw.rectangle([150, 200, 220, 320], fill=color_mangas)

    # Pintar mangas y cuello
    draw.rectangle([30, 90, 80, 160], fill=color_mangas)  # Manga izquierda
    draw.rectangle([220, 90, 270, 160], fill=color_mangas)  # Manga derecha
    draw.rectangle([125, 50, 175, 80], fill=color_cuello)  # Cuello

    # Agregar logo de Ambar
    logo = Image.open("ambar-logo-for-light.png").convert("RGBA")
    logo = logo.resize((70, 30))
    camiseta.paste(logo, (115, 160), logo)

    st.image(camiseta, caption="Vista previa de tu camiseta personalizada", use_column_width=False)
