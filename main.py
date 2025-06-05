import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

st.set_page_config(page_title="🖼️ Image Editor", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #e0f0ff;
        }
        footer {
            visibility: hidden;
        }
        h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }
        .custom-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #007acc;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            z-index: 100;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="custom-footer">
       Developed with 💙 by Mehak Akram | © 2025 🚀
    </div>
""", unsafe_allow_html=True)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def apply_grayscale(image):
    return image.convert("L")

st.title("🖼️ Upload & Edit Your Own Picture")
st.markdown('<label style="color: black; font-weight: 500;">📤 Upload an image</label>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")


if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    st.sidebar.header("🔧 Edit Options")
    brightness = st.sidebar.slider("✨ Brightness", 0.1, 3.0, 1.0, 0.1)
    contrast = st.sidebar.slider("🎨 Contrast", 0.1, 3.0, 1.0, 0.1)
    blur_radius = st.sidebar.slider("🌫️ Blur Radius", 0, 10, 0)
    grayscale = st.sidebar.checkbox("⚫ Apply Grayscale")

    edited_image = adjust_brightness(image, brightness)
    edited_image = adjust_contrast(edited_image, contrast)
    if blur_radius > 0:
        edited_image = apply_blur(edited_image, blur_radius)
    if grayscale:
        edited_image = apply_grayscale(edited_image)

    st.subheader("🖌️ Edited Image")
    st.image(edited_image, use_container_width=True)

    img_bytes = io.BytesIO()
    edited_image.save(img_bytes, format="JPEG")
    st.download_button("📥 Download Edited Image", data=img_bytes.getvalue(), file_name="edited_image.jpg", mime="image/jpeg")
else:
    st.markdown("""
<div style="background-color:#007acc; padding: 10px; border-left: 6px solid #2196F3; border-radius: 5px;">
    <span style="color: pink; font-size: 16px;">👆 Please upload an image to begin editing.</span>
</div>
""", unsafe_allow_html=True)
