import os
import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def assess_risk(age, gender, lifestyle, conditions, translation):
    translations = {
        'Arabic': "Analyze the potential risk factors for developing Alzheimer's disease based on these factors in Arabic:\n"
        # Add more translations as needed
    }
    user_input = translations.get(translation, "Analyze the potential risk factors for developing Alzheimer's disease based on these factors:\n")
    
    if age is not None and age != "":
        user_input += f"Age: {age}\n"

    if gender is not None and gender != "":
        user_input += f"Gender: {gender}\n"

    if lifestyle is not None and lifestyle != "":
        user_input += f"Lifestyle factors: {lifestyle}\n"
    
    if conditions is not None and conditions != "":
        user_input += f"Conditions: {conditions}\n"

    response = model.generate_content(user_input)
    return response.text
    
def main():
    st.title("Cerebra")
    st.image("https://raw.githubusercontent.com/datjandra/cerebra/main/cerebra.png", width=200)
    
    with st.form("user_input_form"):
        # Form fields
        age = st.number_input("Age", min_value=1, max_value=150, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        lifestyle = st.text_input("Lifestyle")
        conditions = st.text_input("Conditions")

        # Translation option
        languages = [None, "Arabic"]
        translation = st.radio("Translate to language:", languages, index=0)
        
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Displaying entered information
        assessment = assess_risk(age, gender, lifestyle, conditions, translation)
        st.markdown(assessment)

if __name__ == "__main__":
    main()
