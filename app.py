import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="AI Writing Coach", page_icon="✍️")
st.title("✍️ AI Writing Coach")
st.write("Enter a paragraph. The AI will correct your grammar, explain your mistakes, and rewrite it in the style you choose.")

# Connect to Gemini using the secret key (saved in Streamlit, not GitHub)
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Inputs
paragraph = st.text_area("Your paragraph", height=200, placeholder="Type or paste your paragraph here...")
style = st.radio("Rewrite style", ["Simple English", "Formal English"], horizontal=True)

# Button
if st.button("Check My Writing", type="primary"):
    if paragraph.strip() == "":
        st.warning("Please enter a paragraph first.")
    else:
        prompt = f"""You are a friendly English writing coach.

Student's paragraph:
{paragraph}

Reply in exactly this format:

## ✅ Corrected Paragraph
(the paragraph with all grammar and spelling mistakes fixed, same meaning)

## 📝 Mistakes Explained
(a numbered list: wrong words → correct words, with a one-line reason)

## ✨ Rewritten in {style}
(the paragraph rewritten in {style})
"""
        with st.spinner("Checking your writing..."):
            try:
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
