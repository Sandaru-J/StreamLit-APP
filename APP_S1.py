import streamlit as st
import re
from pdfminer.high_level import extract_pages, extract_text
import pyttsx3

def text_extraction(file):
    # for page_layout in extract_pages('Employment Contract - Sandaru J.pdf'):
    #     for element in page_layout:
    #         print(element)

    text = extract_text(file)
    # # text_ =text_sampling(text)
    # gen_audio(text)
    # print(text)
    print('Done')
    return text

def gen_audio(text):
    text_s = pyttsx3.init()

    rate = text_s.getProperty('rate')
    text_s.setProperty('rate', 160)

    volume = text_s.getProperty('volume')
    print(volume)
    text_s.setProperty('volume', 1.0)

    voices = text_s.getProperty('voices')
    text_s.setProperty('voice', voices[0].id)
    # text_s.setProperty('voice', voices[1].id)

    # text = 'water is power of life. Are u sure about that?'
    # text_s.say(text)

    text_s.save_to_file(text, 'test.mp3')
    text_s.runAndWait()



def main():
    st.set_page_config(page_title='img 2 audio story')

    st.header('PDF to Audio')
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()  # Read the uploaded file bytes
        text=text_extraction(uploaded_file)  # Pass the bytes to the processing method
        st.success("File uploaded and processed successfully!")

        with st.expander('Text'):
             st.write(text)
        gen_audio(text)
        st.audio('test.mp3')




if __name__ == '__main__':
    main()