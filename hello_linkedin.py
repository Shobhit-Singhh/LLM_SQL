import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


connect_prompt=""
subject_prompt=""
massage_prompt=""
follow_up_prompt=""
def get_gemini_response(prompt, creativity=0.9, p1='NA',p2='NA',p3='NA',p4='NA',p5='NA',p6='NA'):
    generation_config = {
        "temperature": creativity,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
        }
    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
    response = model.generate_content([prompt,prompt,p1,p2,p3,p4,p5,p6])
    return response.text

def app():
    connect,subject,massage = st.tabs(["Connect Massage Draft", "Subject Draft", "Main Massage Draft"])
    with connect:
        col1,col2=st.columns(2)
        with col1:
            with st.form("connect"):
                receiver_name = "receiver name :" + st.text_input("Receiver's Name")
                post = "post to talk about :" + st.text_input('Common Topic of Interest/may be last Post')
                experience = "experience :" + st.text_input("Receiver's Job/Achievement/Project to Talk about")
                custom_connect = "additional info :" + st.text_input("Custom Prompt: 'any other reason to connect to'",'Custom Prompt: Anime, Gaming, Travelling, Gym, Pets, Sports...')
                creativity = st.slider('Creativity', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
                submitted = st.form_submit_button("Submit")

            if submitted:
                with col2:
                    with st.container(height=405, border=True):
                        connect_response = get_gemini_response(connect_prompt, creativity, receiver_name, post, experience, custom_connect)
                        st.text(connect_response)
    
    with subject:
        col3,col4=st.columns(2)
        with col3:
            with st.form("subject"):
                receiver_name = "receiver name :" + st.text_input("Receiver's Name")
                experience = "experience :" + st.text_input("Receiver's Job/Achievement/Project to Talk about")
                sector = "Sector I m targeting :" + st.text_input("Receiver's Sector",)
                skills = "List of Skill Related to this sector :" + st.text_input("Skills might be usefull for Receiver")
                projects = "List of Project Related to this sector :" + st.text_input("Sample of work Your have done in this domain")
                custom_connect = "additional info :" + st.text_input("Custom Prompt: 'any other reason to connect to'",'Custom Prompt: Anime, Gaming, Travelling, Gym, Pets, Sports...')
                creativity = st.slider('Creativity', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
                sub = st.form_submit_button("Submit")
                if sub:
                    with col4:
                        with st.container(height=405, border=True):
                            subject_responce = get_gemini_response(subject_prompt, creativity, receiver_name, experience, sector, skills, projects, custom_connect)
                            st.text(subject_responce)
    
    with massage:
        col3,col4=st.columns(2)
        with col3:
            with st.form("massage"):
                receiver_name = "receiver name :" + st.text_input("Receiver's Name")
                personlization = "common problem :" + st.text_input("Hook/Solution for any common problem",)
                experience = "I'm Skilled in this domain :" + st.text_input("Skills might be usefull for Receiver")
                projects = "List of Project Related to this sector :" + st.text_input("Sample of work Your have done in this domain")
                about_me = "About me:" + st.text_input("Very basic intro")
                custom_connect = "additional info :" + st.text_input("Custom Prompt: 'any other reason to connect to'",'Custom Prompt: Anime, Gaming, Travelling, Gym, Pets, Sports...')
                creativity = st.slider('Creativity', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
                sub = st.form_submit_button("Submit")
                if sub:
                    with col4:
                        with st.container(height=405, border=True):
                            massage_responce = get_gemini_response(massage_prompt, creativity, personlization, receiver_name, experience, projects, about_me, custom_connect)
                            st.text(massage_responce)
                            model = genai.GenerativeModel(model_name="gemini-pro")
                            follow_up = model.generate_content([follow_up_prompt,massage_responce])
                            st.text(follow_up)
        
        
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    api_key = st.sidebar.text_input("Gemini API Key",type='password',help = "Get API Key https://makersuite.google.com/app/apikey'")
    if api_key is not "":
        genai.configure(api_key=api_key)
        app()
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #f1f1f1;
                padding: 2px;
                text-align: center;
                font-size: 14px;
                color: #555;
            }
            .linkedin {
                color: #0077b5;
            }
        </style>
        <div class="footer">
            Data Science App Tutorial by Shobhit Singh, 
            <a class="linkedin" href="https://www.linkedin.com/in/your-linkedin-profile" target="_blank">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )