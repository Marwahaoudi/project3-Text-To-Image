import os
import requests
import streamlit as st
from PIL import Image
import io
from dotenv import load_dotenv
import time  # Pour ajouter un délai

# ✅ Put this first
st.set_page_config(page_title="🖼️ AI Image Generator", page_icon="🎨")

# Load environment variables
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face API URL
api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": f"Bearer {api_key}"}

# 🎨 Customize CSS Style
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;  /* Light grey background */
        }
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

# Main title
st.title("🖼️ AI Image Generator")
st.markdown("Describe what you'd like to generate, and the AI will create an image for you!")

# User input
prompt = st.text_input("📝 Enter a description for the image:")

if st.button("✨ Generate Image") and prompt:
    with st.spinner("⏳ The image is being generated..."):
        # Initialize progress bar and timer
        progress_bar = st.progress(0)
        start_time = time.time()  # Start timer

        data = {
            "inputs": prompt,
            "parameters": {
                "guidance_scale": 7.5,
                "num_inference_steps": 50
            }
        }

        # Simulate the generation process with time and progress update
        for i in range(1, 101):
            time.sleep(0.05)  # Simulate time for generation (for demo purposes)
            progress_bar.progress(i)  # Update the progress bar

        end_time = time.time()  # End timer
        generation_time = round(end_time - start_time, 2)  # Calculate time spent

        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            # Use the container width instead of column width
            st.image(image, caption=f"✅ Image generated successfully ", use_container_width=True)
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
