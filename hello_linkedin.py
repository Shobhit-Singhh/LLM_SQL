import streamlit as st
import os
import genai

connect_prompt="""Your task is to write a LinkedIn Connect massage 
From the set of information given below in 3 sentences

field 1- receiver's name (write the message to the receiver)
field 2- content of the last post (to show interest in the related field)
field 3- Experience/job of Receiver (to show appreciation and respect for his work and want to work under his guidance )
field 4- custom filed (to add any area of interest apart from formal topic)

Example 1:
field 1 - Harshit singh
field 2 - Immediate Requirements of a Data Scientist in our company 
field 3 - job/experience: backend web developer, working on KYC project 
field 4 - common interest/additional info: gaming and Anime

Hi Harshit,

I noticed your job posting for a Data Scientist position and I’m interested in joining your team. With my experience in data science and machine learning. I noticed that you have worked on a KYC project as a backend web developer, and I think you possess a lot of valuable knowledge that I can learn from. I believe that with your guidance and support, I can make a positive contribution to your team. 
Moreover, I couldn't help but notice that we share a common interest in gaming and anime, and I would love to chat with you about our professional and personal interests. 
I have attached my resume for your review. Excited to connect with you.

Example 2:
field 1 - name: Anita singh
field 2 - post to talk about: Looking for a machine learning intern for our company
field 3 - job/experience: Human Resource manager at Google
field 4 - common interest/additional info: Cooking

Hi Anita,

I came across your post that you were seeking a machine learning intern for your company. With my extensive experience in data science and machine learning, I am eager to become a valuable part of your team. I have noticed your exceptional management skills as an HR at Google, and I am hopeful that you will extend the same level of fairness to me. Your reputation precedes you, and I believe that with your guidance and support, I can make a positive contribution to your team.
Moreover, I couldn't help but notice that we share a passion for cooking. I love experimenting with different cuisines, and it would be wonderful to connect and explore our shared interests, both professional and personal.
I have attached my resume for your review. Excited to connect with you.

Example 3:
field 1 - name: Gaurav Kapoor
field 2 - post to talk about: My team have one vacancy for ML ops Engineer to improve Supply Chain efficiency 
field 3 - job/experience: Supply Chain Manager at Amazon
field 4 - common interest/additional info: Travelling and Adventure sports

Hi Gaurav,

I came across your post that Your team have one vacancy for an ML ops Engineer to improve Supply Chain efficiency. As someone experienced in data science and machine learning, I am interested in joining your team. As you are a Supply Chain Manager at Amazon, I am passionate about working under you and your guidance in streamlining supply chain operations. Given my background in data analytics and machine learning, I believe I could bring a fresh perspective to your team and contribute to your innovative work in this field. 
Moreover, I couldn't help but notice that we share an interest in Travelling and Adventure sports. As an avid traveller and adventure enthusiast myself, I would love to connect and share stories about our global explorations and thrilling experiences.
I have attached my resume for your review. Excited to connect with you.


Example 4:
field 1- Shobhit Singh
field 2- looking for a Machine learning intern 
field 3- Senior NLP and MLops Developer
field 4- MS dhoni

Hi Shobhit,

Hello there! Your post seeking a Machine Learning intern for your company got me super excited! I have extensive experience in data science and machine learning, and working under a Senior NLP and MLops Developer is a dream come true! I can’t wait to join your team and learn from your exceptional skills and expertise in the field. 
Moreover, I couldn't help but notice that we share a common admiration for MS Dhoni. I think that’s fantastic! It would be great to connect with you and chat about our personal and professional interests. 
I have attached my resume for your review. Thank you for considering my application. I look forward to hearing from you soon!

Example 5:
field 1 - Anjali Shekhar
field 2 - need a trainee for fine-tuning LLM
field 3 - Human Resource manager at Amazon 
field 4 - Virat Kohli 
Hi Anjali,

I saw your post that you are looking for a trainee to assist with fine- tuning LLM. I am excited about this opportunity to join your team. Being an accomplished Human Resource Manager at Amazon, I am hopeful of receiving the same fairness and guidance from you. I am sure I can make valuable contributions to your team with your support and mentorship. 
Moreover, I couldn't help but notice that we share a common interest in Virat Kohli, which is amazing! I would love to connect and discuss our professional and personal interests further. 
I have attached my resume for your review. Thank you for giving me an opportunity to work under your guidance.

Example 6:
field 1 - Sameer Mehta
field 2 - PO hiring for AI-powered social-emotional learning platform 
field 3 - Product Manager at Google (AI/ML)
field 4 - Veganism

Hi Sameer,

I came across your post regarding the Product Owner position for your AI-powered social-emotional learning platform. I am thrilled to apply for this role, given my background in data science and machine learning. Having worked as a Product Manager at Google in the AI/ML space, your expertise and leadership are well-known in the field. I believe that your guidance will be invaluable as I navigate the challenges of this position and contribute to your team’s success. 
Moreover, I couldn't help but notice that we share a common interest in Veganism. It's a fantastic coincidence! I would love to connect with you to discuss our professional goals and personal interests further.
I have attached my resume for your reference. Thank you for taking the time to consider my application."""

massage_prompt="""
Your task is to write a message
From the set of information given below in 3 sentences

note: field 7 list of project will be in separate line with there hyperlinks


field 1 - Receiver's name (Write the message to the receiver):
field 2 - company's name:
field 3 - common problem and solution (Hook/Solution for any common problem):
field 4 - Company history (Company working history/sector):
field 5 - Job Description (to find out the machine skill):
field 6 - List of skills related to this sector (List of Sector related skills I have):
field 7 - List of projects related to this sector (To Show my hands-on experience):
field 8 - About me (My introduction)  

Example 1: 

field 1 - Harshit Singh 
field 2 - MLP 
field 3 - what if you don’t need to write a single line of code for Data Processing, EDA, Feature Engineering, Not even for Hyperparameter tuning  
field 4 - As your company is closely working with health data and has a huge flow of data every day 
field 5 - Data Analysis and Exploration, Model Development, Data Cleaning and Preprocessing, Feature Engineering, Communication and Visualization
field 6 - Machine learning, Deep Learning, NLP, LLM Finetuning, Prompt Engineering, Web Scraping, Dashboard, MLops, SQL, DSA
field 7 - All-in-one Data Science App, a Dashboard to Monitor customer churn, a Questions Generation model from text using NLP, a LinkedIn assistant using LLM, code forces rating 1200+, leet code rating 1500+
field 8 - Greetings! I’m Shobhit Kumar Singh, a seasoned data scientist and machine learning enthusiast with numerous certifications and successful projects. I’m eager to join your team and contribute my expertise to help achieve your goals.

Response-
Subject: Effortlessly processing data, conducting EDA, feature engineering, and hyperparameter tuning without writing any code!
Dear Harshit singh,
Imagine solving a common challenge in the field of Data analysis without writing a single line of code for Data Preprocessing, EDA, Feature Engineering, or even Hyper-parameter tuning. That's the innovation I bring to the table, and I believe it could greatly benefit your team at MLP.
Considering MLP rich history of closely working with health data and handling substantial daily data flows.

My expertise in Data Analysis, Exploration, Model Development, Data Cleaning and Preprocessing, Feature Engineering, and effective Communication and Visualization align seamlessly with your needs.
My proficiency extends to a diverse set of skills, including 
Machine Learning, Deep Learning, NLP, LLM Fine-tuning, Prompt Engineering, Web Scraping, Dashboard creation, ML-ops, SQL, and Data Structures and Algorithms.
I have hands-on experience showcased through projects like 
The all-in-one Data Science App - Link
Dashboard to Monitor customer churn - Link
Questions Generation model from text using NLP - Link
LinkedIn assistant using LLM - Link

Additionally, my competitive programming achievements, with a CodeForces rating of 1200+ and LeetCode rating of 1500+, underline my commitment to excellence.
Allow me to introduce myself: I'm Shobhit Kumar Singh, a seasoned data scientist and machine learning enthusiast with numerous certifications and a track record of successful projects. I’m eager to join your team and contribute my expertise to help achieve your goals.
I know you’re very busy, but I would be thrilled if you could spare just 300 seconds of your time to hear me out. I truly believe that I could be a valuable asset to your team, and I’m eager to share my thoughts with you. If it’s not too much trouble, could you connect me with someone on your team so we can discuss this further?
I look forward to the opportunity to discuss how my skills and experience can contribute to the success of your team at MLP.
Best Regards,
Shobhit Kumar Singh

Example 2: 

Field 1 - Emily Thompson
Field 2 - XYZ Tech
Field 3 - Tired of struggling with manual testing and debugging? Imagine a seamless automated testing process that ensures robust software quality.
Field 4 - With a rich history of pioneering software solutions in the tech industry for over a decade, XYZ Tech's commitment to innovation aligns perfectly with my skills and experience.
Field 5 - Automated Testing, Debugging, Software Development, Continuous Integration
Field 6 - Python, Java, Selenium, JUnit, TestNG, Jenkins, Git, DevOps
Field 7 - Automated Testing Framework for E-commerce Website, Continuous Integration Pipeline for Mobile App, Bug Tracking System Enhancement, Jenkins Plugin Development
Field 8 - Hello, I'm John Doe, an accomplished Senior Software Engineer specializing in automated testing and continuous integration. With a track record of successful projects and a strong background in software development, I am excited about the opportunity to contribute to XYZ Tech's continued success.

Response-
Subject: Elevating Software Quality through Automated Testing Expertise
Dear Emily Thompson,
Tired of struggling with manual testing and debugging? Imagine a seamless automated testing process that ensures robust software quality. As a specialist in automated testing and continuous integration, I am excited about the opportunity to contribute my expertise to XYZ Tech.
With a rich history of pioneering software solutions in the tech industry for over a decade, XYZ Tech's commitment to innovation aligns perfectly with my skills and experience. 

My proficiency in Automated Testing, Debugging, Software Development, and Continuous Integration positions me as a valuable asset to enhance your team's efficiency.
I bring a diverse set of skills, including expertise in 
Python, Java, Selenium, JUnit, TestNG, Jenkins, Git, and DevOps. 
My hands-on experience is highlighted through projects such as 
Automated Testing Framework for an E-commerce Website - Link
Continuous Integration Pipeline for a Mobile App - Link
Enhancements to a Bug Tracking System, along with Jenkins Plugin Development - Link

Allow me to introduce myself: I'm John Doe, an accomplished Senior Software Engineer with a track record of successful projects and a strong background in software development. I am eager to bring my skills and passion for automated testing to XYZ Tech, contributing to its continued success.
I know you’re very busy, but I would be thrilled if you could spare just 300 seconds of your time to hear me out. I truly believe that I could be a valuable asset to your team, and I’m eager to share my thoughts with you. If it’s not too much trouble, could you connect me with someone on your team so we can discuss this further?
I look forward to the opportunity to discuss how my expertise can elevate software quality within XYZ Tech.
Best Regards,
John Doe


Example 3: 

Field 1 - Samantha Rodriguez
Field 2 - TechGenius Inc.
Field 3 - Struggling with user engagement? Elevate your product with an intuitive design that captivates users and enhances their overall experience.
Field 4 - TechGenius Inc. has a history of revolutionizing user experiences across various industries, and my design expertise can further enhance your company's reputation for cutting-edge innovation.
Field 5 - UX/UI Design, Prototyping, User Research, Interaction Design, Wireframing
Field 6 - Adobe Creative Suite, Figma, Sketch, InVision, User Testing, Responsive Design, UI Animation
Field 7 - Redesigned Mobile Banking App for Improved Accessibility, E-commerce Website with 20% Increase in Conversion Rate, Interactive Dashboard for Data Visualization
Field 8 - Greetings! I'm Samantha Rodriguez, a seasoned UX/UI designer with a proven track record of transforming concepts into visually appealing and user-friendly designs. My passion for creating exceptional user experiences aligns seamlessly with the vision of TechGenius Inc., and I am eager to contribute my skills to drive your company's success.

Response-
Subject: Elevate User Engagement through Innovative UX/UI Design
Dear Samantha Rodriguez,
Struggling with user engagement? Elevate your product with an intuitive design that captivates users and enhances their overall experience. I am excited about the opportunity to contribute my expertise to TechGenius Inc.
TechGenius Inc. has a history of revolutionizing user experiences across various industries, and my design expertise can further enhance your company's reputation for cutting-edge innovation. 

My proficiency in UX/UI Design, Prototyping, User Research, Interaction Design, and Wireframing positions me as a valuable asset to amplify your team's creative capabilities.
I bring a diverse set of skills, including mastery of 
Adobe Creative Suite, Figma, Sketch, InVision, User Testing, Responsive Design, and UI Animation. 
My hands-on experience is demonstrated through projects such as the 
Redesigned Mobile Banking App for Improved Accessibility - Link
an E-commerce Website with a 20% Increase in Conversion Rate - Link
an Interactive Dashboard for Data Visualization - Link

Allow me to introduce myself: I'm Samantha Rodriguez, a seasoned UX/UI designer with a proven track record of transforming concepts into visually appealing and user-friendly designs. My passion for creating exceptional user experiences aligns seamlessly with the vision of TechGenius Inc., and I am eager to contribute my skills to drive your company's success.
I know you’re very busy, but I would be thrilled if you could spare just 300 seconds of your time to hear me out. I truly believe that I could be a valuable asset to your team, and I’m eager to share my thoughts with you. If it’s not too much trouble, could you connect me with someone on your team so we can discuss this further?
I look forward to the opportunity to discuss how my expertise can elevate user engagement and design innovation within TechGenius Inc.
Best Regards,
Samantha Rodriguez

Example 4: 

Field 1 - Alex Turner
Field 2 - InnovateTech Solutions
Field 3 - Overwhelmed by inefficient coding processes? Streamline your development workflow with optimized coding practices and innovative solutions.
Field 4 - InnovateTech Solutions has a remarkable history of delivering groundbreaking software solutions, and my extensive experience in software development can bring valuable insights to your dynamic team.
Field 5 - Full Stack Development, Agile Methodology, Code Optimization, System Architecture, DevOps
Field 6 - JavaScript, Python, React, Node.js, Docker, Git, RESTful APIs, MongoDB
Field 7 - Implemented Microservices Architecture for Scalability, Developed Real-time Chat Application, Automated Deployment Pipeline for Faster Releases
Field 8 - Hello! I'm Alex Turner, a seasoned Senior Software Developer with a passion for creating efficient and scalable solutions. Having successfully led projects that embraced cutting-edge technologies, I am excited about the opportunity to contribute to InnovateTech Solutions and drive innovation in your development processes.

Response-
Subject: Streamlining Development Processes for InnovateTech Solutions
Dear Alex Turner,
Overwhelmed by inefficient coding processes? Streamline your development workflow with optimized coding practices and innovative solutions. I am excited about the opportunity to contribute my extensive experience in software development to InnovateTech Solutions.
InnovateTech Solutions has a remarkable history of delivering groundbreaking software solutions, and my expertise in Full Stack Development, Agile Methodology, Code Optimization, System Architecture, and DevOps can bring valuable insights to your dynamic team. I am confident that my skills align seamlessly with your company's commitment to innovation.

I bring a diverse set of skills, including proficiency in 
JavaScript, Python, React, Node.js, Docker, Git, RESTful APIs, and MongoDB. 

My hands-on experience is showcased through projects such as the 
implementation of Microservices Architecture for Scalability - Link
the development of a Real-time Chat Application - Link
the establishment of an Automated Deployment Pipeline for Faster Releases - Link

Allow me to introduce myself: I'm Alex Turner, a seasoned Senior Software Developer with a passion for creating efficient and scalable solutions. Having successfully led projects that embraced cutting-edge technologies, I am excited about the opportunity to contribute to InnovateTech Solutions and drive innovation in your development processes. I know you’re very busy, but I would be thrilled if you could spare just 300 seconds of your time to hear me out. I truly believe that I could be a valuable asset to your team, and I’m eager to share my thoughts with you. If it’s not too much trouble, could you connect me with someone on your team so we can discuss this further?
I look forward to the opportunity to discuss how my expertise can streamline development processes and contribute to the success of InnovateTech Solutions.
Best Regards,
Alex Turner

Example 5: 

Field 1 - Olivia Martinez
Field 2 - Quantum Innovations, Data Science Lead
Field 3 - Struggling to extract meaningful insights from your data? Unleash the power of data science to drive informed decision-making and enhance your business strategies.
Field 4 - Quantum Innovations, with a proven track record in harnessing the potential of data, is the perfect match for my skills and experience in data science. Together, we can elevate your data-driven approach to a new level of excellence.
Field 5 - Predictive Modeling, Machine Learning, Data Visualization, Statistical Analysis, Big Data Processing
Field 6 - Python, R, TensorFlow, Tableau, SQL, Hadoop, Pandas, Scikit-Learn
Field 7 - Customer Churn Prediction Model, Fraud Detection System, Interactive Dashboard for Sales Analytics, Sentiment Analysis on Social Media Data
Field 8 - Greetings! I'm Olivia Martinez, an accomplished Data Science Lead with a passion for transforming raw data into actionable insights. With a history of successful projects and expertise in cutting-edge technologies, I am eager to bring my skills to Quantum Innovations and contribute to the advancement of your data science capabilities.

Response-
Subject: Elevating Data-driven Strategies with Expert Data Science Leadership

Dear Olivia Martinez,
Struggling to extract meaningful insights from your data? Unleash the power of data science to drive informed decision-making and enhance your business strategies. As an accomplished Data Science Lead, I am excited about the opportunity to contribute my skills and experience to Quantum Innovations.
Quantum Innovations, with a proven track record in harnessing the potential of data, is the perfect match for my expertise in Predictive Modeling, Machine Learning, Data Visualization, Statistical Analysis, and Big Data Processing. Together, I believe we can elevate your data-driven approach to a new level of excellence.
I bring a diverse set of skills, including proficiency in 

Python, R, TensorFlow, Tableau, SQL, Hadoop, Pandas, and Scikit-Learn. 

My hands-on experience is exemplified through projects such as 
Customer Churn Prediction Model - Link
Fraud Detection System - Link
Interactive Dashboard for Sales Analytics - Link
Sentiment Analysis on Social Media Data - Link

Allow me to introduce myself: I'm Olivia Martinez, an accomplished Data Science Lead with a passion for transforming raw data into actionable insights. With a history of successful projects and expertise in cutting-edge technologies, I am eager to bring my skills to Quantum Innovations and contribute to the advancement of your data science capabilities.
I know you’re very busy, but I would be thrilled if you could spare just 300 seconds of your time to hear me out. I truly believe that I could be a valuable asset to your team, and I’m eager to share my thoughts with you. If it’s not too much trouble, could you connect me with someone on your team so we can discuss this further? 
I’m passionate about the potential to enhance Quantum Innovations’ data-driven strategies with my leadership and data science skills, and I’m confident that we could achieve great things together.

Best Regards,
Olivia Martinez
"""

def get_gemini_response(prompt, creativity=0.9, p1='NA',p2='NA',p3='NA',p4='NA',p5="",p6="",p7="",p8=""):
    generation_config = {
        "temperature": creativity,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
        }
    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
    response = model.generate_content([prompt,p1,p2,p3,p4,p5,p6])
    return response.text

def app():
    connect,massage = st.tabs(["Connect Massage Draft","Main Massage Draft"])
    with connect:
        col1,col2=st.columns(2)
        with col1:
            with st.form("connect"):
                receiver_name = "field 1 - Name: " + st.text_input("Receiver's Name")
                post = "field 2 - Job post details: " + st.text_input('Job description/or title ')
                experience = "field 3 -  Job/experience: " + st.text_input("Receiver's Job/Achievement/Project to Talk about")
                custom_connect = "field 4 -  Common interest/additional info: " + st.text_input("Common interest (if any)")
                creativity = st.slider('Creativity', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
                submitted = st.form_submit_button("Submit")

            if submitted:
                with col2:
                    with st.container(height=505, border=True):
                        st.write(receiver_name)
                        st.write(post)
                        st.write(experience)
                        st.write(custom_connect)
                        st.markdown("---")
                        connect_response = get_gemini_response(connect_prompt, creativity, receiver_name, post, experience, custom_connect)
                        st.write(connect_response)
    
    with massage:
        col3,col4=st.columns(2)
        with col3:
            with st.form("massage"):
                receiver_name = "field 1 - Name of receiver: " + st.text_input("Receiver's Name")
                company = "field 2 - Name of receiver: " + st.text_input("Company Name")
                personlization = "field 3 - Common problem: " + st.text_input("Hook/Solution for any common problem")
                company_history = "field 4 - Company history: " + st.text_input("Company working history/sector")
                job_desc = "field 5 - Job Description: " + st.text_input("Required Skills/Job Description")
                skills = "field 6 - List of Skill Related to this sector: " + st.text_input("Your Skills")
                projects = "field 7 - List of Project Related to this sector: " + st.text_input("Project")
                about_me = "field 8 - About me: " + st.text_input("Introduction")
                creativity = st.slider('Creativity', min_value=0.0, max_value=1.0, value=0.9, step=0.01)
                sub = st.form_submit_button("Submit")

                if sub:
                    with col4:
                        with st.container(height=840, border=True):
                            st.write(receiver_name)
                            st.write(company)
                            st.write(personlization)
                            st.write(company_history)
                            st.write(job_desc)
                            st.write(skills)
                            st.write(projects)
                            st.write(about_me)
                            st.markdown("---")
                            subject_responce = get_gemini_response(massage_prompt, creativity, receiver_name, company, personlization, company_history, job_desc, skills, projects, about_me)
                            st.write(subject_responce)
                            model = genai.GenerativeModel(model_name="gemini-pro")

        
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    api_key = st.sidebar.text_input("Gemini API Key",type='password',help = "Get API Key https://makersuite.google.com/app/apikey")
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