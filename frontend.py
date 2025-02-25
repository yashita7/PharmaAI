import streamlit as st
import asyncio
from main import process_prescription

# Streamlit UI
st.set_page_config(page_title="Pharmacist Assistant", layout="centered")

st.title("💊 Pharmacist Assistant")
st.write("Upload a prescription image, and our AI will extract and analyze the medical information.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload Prescription Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Save uploaded image temporarily
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(image_path, caption="Uploaded Prescription", use_column_width=True)
    st.write("🔍 Processing...")
    
    # Run async process
    result = asyncio.run(process_prescription(image_path))
    
    # Display results
    st.subheader("🤖 Analysis Result:")
    st.write(result)

    # Remove temp file after processing (optional)
    import os
    os.remove(image_path)
