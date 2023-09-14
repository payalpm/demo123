import streamlit as st
# st.title("hello, Streamlit")
# st.write("Welcome ton your first streamlit web application.")
# user_input = st.text_input("Please enter ur name")
# if user_input:
#     st.write("hello",{user_input})
# if st.button("click me!"):
#     st.write("u clicked the button")
# st.sidebar.header("about")
# st.sidebar.text("hy my name is payal.")
# csv excel files show kar sakhte hai

# web application form
st.title("simple web form application")
with st.form("user information"):
    name = st.text_input("enter ur name")
    email = st.text_input("enter ur email")
    gender = st.radio("select ur gender", ("male","female","other"))
    agree = st.checkbox("i agree to terms and conditions")
    submit_button = st.form_submit_button("submit")
if submit_button:
    st.write("u submitted the following information:")
    st.write(f"name: {name}")
    st.write(f"email: {email}")
    st.write(f"gender: {gender}")
    st.write("agree to terms & conditions: yes" if agree else "agreed to terms& conditions: No")

