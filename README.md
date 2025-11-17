# AI Marketing Campaign Generator

This project is a simple web application that generates marketing content based on user inputs.
It uses:

* **Gemini (Google AI)** for generating ad copy
* **Hugging Face Stable Diffusion XL** for generating images
* **Streamlit** for the user interface

Users provide a product description and target audience, and the app generates:

* A short marketing ad
* A creative image
* An option to download the generated image

---

## Features

* Generates marketing ad copy using Gemini
* Creates high-quality images using Hugging Face SDXL
* Clean, lightweight UI built with Streamlit
* No local machine learning models required
* Works smoothly on Streamlit Cloud

---

## Tech Stack

* Python
* Streamlit
* google-genai
* Hugging Face Inference API

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Add your API keys in Streamlit secrets (local `secrets.toml` or Streamlit Cloud):

```
GEMINI_API_KEY = "your_gemini_api_key"
STABLE_DIFFUSION_API_KEY = "your_huggingface_api_key"
```

---

## Running the App

```bash
streamlit run app.py
```

---

## Deployment

1. Push the project to GitHub
2. Open Streamlit Cloud
3. Deploy the app
4. Add the API keys in Streamlit Secrets
5. Run the app

