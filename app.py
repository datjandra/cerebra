import streamlit as st

def main():
    st.title("Form with Streamlit")

    with st.form("user_input_form"):
        # Form fields
        age = st.number_input("Age", min_value=0, max_value=150, step=1, value=25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        lifestyle = st.text_input("Lifestyle")
        conditions = st.text_input("Conditions")

        # Translation option
        translation = st.radio("Translate to", ["Arabic", "Urdu"])

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Displaying entered information
        st.write("Entered Information:")
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("Lifestyle:", lifestyle)
        st.write("Conditions:", conditions)

if __name__ == "__main__":
    main()
