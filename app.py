import streamlit as st
import requests
from gtts import gTTS
from google import genai

# Initialize Gemini client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🚀 AI Marketing Campaign Generator")

product_desc = st.text_area("📝 Enter Product Description")
target_audience = st.text_area("🎯 Enter Target Audience")

if st.button("Generate Campaign"):
    if product_desc and target_audience:
        # Generate Dynamic Ad Copy via Gemini
        prompt = f"Write a catchy, engaging marketing ad for '{product_desc}' targeted at '{target_audience}'. Keep it short and appealing."
        with st.spinner("Generating ad copy..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",  # Specify Gemini model
                contents=prompt
            )
            ad_copy = response.text.strip()
        
        st.subheader("📢 Generated Ad Copy")
        st.write(ad_copy)

        # Generate Image via Hugging Face SDXL API
        st.subheader("Generated Creative")
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": f"Bearer {st.secrets['STABLE_DIFFUSION_API_KEY']}"}
        image_prompt = f"{product_desc}, targeted for {target_audience}"
        data = {"inputs": image_prompt}

        with st.spinner("⏳ Generating image..."):
            response = requests.post(API_URL, headers=headers, json=data)
            if response.status_code == 200:
                with open("creative.png", "wb") as f:
                    f.write(response.content)
                st.image("creative.png", caption="Generated Creative", use_container_width=True)
                with open("creative.png", "rb") as f:
                    st.download_button("⬇ Download Image", f, file_name="creative.png")
            else:
                st.error(f"Image generation failed: {response.status_code}\n{response.text}")

        # Generate Audio Ad
        st.subheader("🎧 Audio Ad")
        tts = gTTS(ad_copy)
        tts.save("ad_audio.mp3")
        with open("ad_audio.mp3", "rb") as f:
            st.audio(f.read(), format="audio/mp3")
            st.download_button("⬇ Download Audio", f, file_name="ad_audio.mp3")

    else:
        st.warning("⚠ Please fill in both product description and target audience.")
