import os
import requests
import streamlit as st
from PIL import Image
import io
from dotenv import load_dotenv
import time

# Configuration de la page
st.set_page_config(page_title="AI Image Generator", page_icon="🖼️ ")

# Chargement de la clé API depuis .env
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

# URL de l'API Hugging Face
api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": f"Bearer {api_key}"}

# Personnalisation CSS
st.markdown("""
    <style>
        .stButton > button {
            background-color: #6c63ff;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .stImage > img {
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.title("🖼️  Générateur d'images par IA")
st.markdown("Décris une image que tu veux créer, l'IA va la générer pour toi !")

#  Colonnes pour l'entrée
col1, col2 = st.columns([3, 1])

with col1:
    prompt = st.text_input("📝 Description de l’image :")

with col2:
    guidance = st.slider("🎯 Guidance", 1.0, 20.0, 7.5, step=0.5)

# Paramètres supplémentaires
num_inference_steps = st.slider("🧠 Étapes d’inférence", 10, 100, 50, step=10)

# Exemples
examples = [
    "A magical forest with glowing trees",
    "A futuristic robot painting a canvas",
    "A dragon flying over a medieval city",
    "An astronaut relaxing on Mars",
]
example = st.selectbox("💡 Choisir un exemple :", [""] + examples)
if example:
    prompt = example

# Historique
if "history" not in st.session_state:
    st.session_state.history = []

# Génération de l’image
if st.button("✨ Générer l’image") and prompt:
    with st.spinner("⏳ Génération de l’image en cours..."):
        progress_bar = st.progress(0)
        start_time = time.time()

        data = {
            "inputs": prompt,
            "parameters": {
                "guidance_scale": guidance,
                "num_inference_steps": num_inference_steps
            }
        }

        # Effet de progression simulée
        for i in range(1, 101):
            time.sleep(0.01)
            progress_bar.progress(i)

        # Requête vers l'API Hugging Face
        response = requests.post(api_url, headers=headers, json=data)
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        if response.status_code == 200:
            image_bytes = io.BytesIO(response.content)
            image = Image.open(image_bytes)

            st.image(image, caption=f"✅ Image générée en {duration}s", use_container_width=True)
            st.success("Image générée avec succès !")

            #  Bouton de téléchargement
            st.download_button(
                label="📥 Télécharger l’image",
                data=image_bytes,
                file_name="image_ai.png",
                mime="image/png"
            )

            #  Sauvegarde dans l'historique
            st.session_state.history.append((prompt, image))

        else:
            st.error(f"❌ Erreur {response.status_code}: {response.text}")

# Affichage de l'historique
if st.session_state.history:
    st.markdown("## 🕓 Historique")
    for old_prompt, old_image in reversed(st.session_state.history[-3:]):
        st.image(old_image, caption=f"📝 {old_prompt}", use_container_width=True)
