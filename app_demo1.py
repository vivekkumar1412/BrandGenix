import streamlit as st
#from ai_service import generate_brand_names, generate_marketing_content
from app.ai_service import generate_brand_names, generate_marketing_content
# Page config
st.set_page_config(
    page_title="BrandGenix AI",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 BrandGenix AI")
st.caption("AI-powered Brand Name & Content Generator")

# ------------------------------
# BRAND NAME GENERATION
# ------------------------------
st.header("🔤 Brand Name Generator")

brand_prompt = st.text_input(
    "Describe your startup idea",
    placeholder="AI startup that builds smart assistants"
)

n_names = st.slider("Number of brand names", 1, 10, 3)

if st.button("Generate Brand Names"):
    if brand_prompt.strip() == "":
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Generating brand names..."):
            result = generate_brand_names(brand_prompt, n_names)

        st.success("Brand names generated!")
        st.markdown(result)

# ------------------------------
# CONTENT GENERATION
# ------------------------------
st.header("📝 Marketing Content Generator")

brand_description = st.text_area(
    "Brand description",
    placeholder="AI startup that builds smart assistants"
)

tone = st.selectbox(
    "Tone",
    ["professional", "friendly", "fun", "formal"]
)

content_type = st.selectbox(
    "Content type",
    ["product description", "website copy", "social media post"]
)

language = st.selectbox(
    "Language",
    ["en", "es", "fr"]
)

if st.button("Generate Content"):
    if brand_description.strip() == "":
        st.warning("Please enter a brand description.")
    else:
        with st.spinner("Generating content..."):
            content = generate_marketing_content(
                brand_description,
                tone,
                content_type,
                language
            )

        st.success("Content generated!")
        st.markdown(content)

st.markdown("---")
st.caption("Built for Hackathon Demo 💡")
