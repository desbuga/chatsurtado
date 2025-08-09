import streamlit as st
import random
import os

# Config da página
st.set_page_config(page_title="DesbugaXuxu", layout="centered")

# Título
st.title("🧠 DesbugaXuxu — Modo Ravena")
st.markdown("Parece fofo, mas é bugado com propósito. 🖤🚂")

# Frases do dia
frases = [
    "Teoria do Caos: nada é tão ruim que não possa piorar.",
    "Quem nunca falou com a parede, nunca tentou programar sem café.",
    "Não é bug, é revolta programada.",
    "Calma é pra quem tem tempo. Aqui é pressão e bug.",
    "Se melhorar, estraga. Se travar, reinicia a mente."
]
st.markdown(f"💥 Frase do dia: _{random.choice(frases)}_")

# Pasta de áudios
AUDIO_DIR = "audios/revolts"
if os.path.exists(AUDIO_DIR):
    audios = [f for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]
    if audios:
        audio_file = st.selectbox("Escolha um áudio", audios)
        if st.button("▶️ Tocar áudio"):
            audio_path = os.path.join(AUDIO_DIR, audio_file)
            with open(audio_path, "rb") as f:
                st.audio(f.read(), format="audio/mp3")
    else:
        st.warning("Nenhum áudio encontrado na pasta.")
else:
    st.error("Pasta de áudio não encontrada.")

st.success("Tudo nos trilhos, Xuxu! 🚂")
