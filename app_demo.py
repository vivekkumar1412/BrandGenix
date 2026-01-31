import streamlit as st
from ai_service import generate_brand_names, generate_marketing_content

st.set_page_config(page_title="BrandGenix AI", layout="wide")
st.title("BrandGenix AI Hackathon Demo")

# User input
brand_prompt = st.text_input("Enter your AI startup idea:", "AI startup")

# Number of brand names
n_names = st.number_input("How many brand names?", min_value=1, max_value=10, value=3)

if st.button("Generate Brand Names"):
    with st.spinner("Generating brand names..."):
        brand_names = generate_brand_names(brand_prompt, n_names)
    st.success("Done!")
    st.subheader("Brand Names:")
    st.write(brand_names)

# Optional: Content generation
st.subheader("Generate Marketing Content")
brand_desc = st.text_area("Enter brand description:", "AI startup that builds smart assistants")
tone = st.selectbox("Tone", ["professional", "friendly", "fun", "formal"])
content_type = st.selectbox("Content Type", ["product description", "social post", "website copy"])
language = st.selectbox("Language", ["en", "es", "fr"])

if st.button("Generate Content"):
    with st.spinner("Generating marketing content..."):
        content = generate_marketing_content(brand_desc, tone, content_type, language)
    st.success("Done!")
    st.subheader("Generated Content:")
    st.write(content)
