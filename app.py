import streamlit as st
from transformers import pipeline

def main():
    # Set up the title of the app
    st.title("English to Chinese Translation")

    # Load a translation model from Hugging Face
    translator = pipeline('translation_en_to_zh', model='Helsinki-NLP/opus-mt-en-zh')

    # Custom CSS to style the app
    st.markdown("""
        <style>
        .main {
            background-color: #fff8e5;
        }
        .stTextArea>div>div>textarea {
            border: 2px solid #d9ead3;
            border-radius: 10px;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border-radius: 20px;
            border: none;
            padding: 10px 24px;
        }
        .result-container {
            border: 2px solid #d9ead3;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Create a text input for user queries
    user_input = st.text_area("Enter English text to translate to Chinese:", value='', height=250, max_chars=500)

    if st.button('Translate'):
        if user_input:
            # Translate the text using the model
            translation = translator(user_input, max_length=400)
            st.markdown(f"<div class='result-container'>Translated text:<br>{translation[0]['translation_text']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-container'>Error:<br>{'Please enter some text.'}</div>",
                        unsafe_allow_html=True)

if __name__ == '__main__':
    main()
