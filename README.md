# Project3: Text-to-Image
## 🎬 Project Presentation

Click the image below to watch the project demo video:

[Watch the video](https://drive.google.com/file/d/1Y1eaE1CQCGnH5xZRCyHtrKVLRv2Y_Jbl/view?usp=sharing)

## 🌐 Hosted Application

The application is deployed on **Streamlit Cloud**.  
[Click here to access the Text-to-Image App](https://project3-text-to-image-knncbxtbscvuedsbaugxp4.streamlit.app/)

---

## Description

This application allows users to generate images from textual descriptions (prompts) using the Hugging Face API.  
It is built with Python and Streamlit, offering a simple and interactive interface for testing text-to-image generation

## Overview
This project implements a Text-to-Image generation app using the Hugging Face Inference API. Users can input a prompt (e.g., "a futuristic city at sunset") and receive a generated image using a pre-trained model.

The goal is to demonstrate how to connect a front-end interface built with Streamlit to a Hugging Face model and create a smooth and responsive user experience.

## Project Members

- **Hanane Saidi**
- **Marwa Haoudi**

## Technologies Used

- Python 3.12
- Streamlit – Web app interface
- Hugging Face Inference API – Model hosting and inference
- Requests – HTTP requests to API
- dotenv – Secure handling of API tokens
- Pillow – Image processing and visualizatio
## Environment Setup 
### 1. Clone the Project from GitHub

Make sure git is installed.  
In your terminal or Anaconda Prompt:

```bash
git clone https://github.com/Marwahaoudi/project3-Text-To-Image.git
cd project3-Text-To-Image.git
```
### 2. Install Required Libraries
 ```bash
pip install -r requirements.txt

```
### 3. Add Hugging Face API Token
Create a .env file with the following content:
 ```bash
HF_TOKEN=your_token_here
```
## Objectives
- Build an interactive front-end for text-to-image generation
- Learn to use Hugging Face's Inference API in production
- Handle asynchronous image generation and display in real time
- Develop an intuitive and accessible UI with Streamlit

## Architecture

 ```bash
User ➜ Streamlit Interface ➜ Hugging Face API ➜ Generated Image
```
- User enters a prompt.
- Streamlit sends the request with token to Hugging Face.
- The API returns the image.
- Streamlit displays the image.

## 🖼️ Example Outputs

| Prompt                        | Generated Image |
|------------------------------|-----------------|
| *"A cute cat wearing glasses reading a book"*   | ![Example 1](images/t2.PNG) |
| *"A wizard casting a spell in a glowing forest"* | ![Example 2](images/T4.PNG) |
| *"Abstract colorful shapes in the style of modern art"* | ![Example 2](images/T3.PNG) |

> Tip: Create a folder named `images/` in your project directory and place sample output images there (e.g., `t2.png`, `T4.png`). This helps users visualize what the app can generate.

## Features

- Enter any text prompt to generate an image
- Uses pre-trained models via Hugging Face Inference API
- Simple and clean Streamlit interface
- Hosted online with easy access
- API token handling via .env for security

## Acknowledgments

- Our module instructor, Abdelhak Mahmoudi, for his guidance and support throughout the project.

