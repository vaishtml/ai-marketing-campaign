import streamlit as st
import requests
from google import genai
from io import BytesIO

# Initialize Gemini Client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("AI Marketing Campaign Generator")

product_desc = st.text_area("Product Description")
target_audience = st.text_area("Target Audience")


if st.button("Generate Campaign"):
    if product_desc and target_audience:

        # 1. Generate Ad Copy (Gemini)
        ad_prompt = (
            "You are an expert marketing copywriter. "
            "Write a short, catchy, high-converting promotional message for the following product:\n\n"
            f"Product: {product_desc}\n"
            f"Target Audience: {target_audience}\n\n"
            "Tone: modern, engaging, persuasive.\n"
            "Length: 1–2 sentences.\n"
            "Avoid clichés and make it sound fresh and appealing."
        )

        with st.spinner("Generating ad copy..."):
            ad_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ad_prompt
            )
            ad_copy = ad_response.text.strip()

        st.subheader("Generated Ad Copy")
        st.write(ad_copy)


        # 2. Generate Image via Hugging Face SDXL
        st.subheader("Generated Creative")

        API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": f"Bearer {st.secrets['STABLE_DIFFUSION_API_KEY']}"}
        payload = {"inputs": f"{product_desc}, targeted for {target_audience}"}

        with st.spinner("Generating image..."):
            img_response = requests.post(API_URL, headers=headers, json=payload)

            if img_response.status_code == 200:
                image_bytes = img_response.content

                # Display image
                st.image(image_bytes, caption="Generated Creative", use_container_width=True)

                # Download button
                st.download_button(
                    "Download Image",
                    data=image_bytes,
                    file_name="generated_image.png",
                    mime="image/png"
                )

            else:
                st.error(f"Image generation failed: {img_response.status_code}\n{img_response.text}")

    else:
        st.warning("Please fill in both product description and target audience.")
