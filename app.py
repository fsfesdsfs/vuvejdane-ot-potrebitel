import streamlit as st

st.write("Колко е 5 + 3?")


user_answer = st.number_input("Въведете отговора:", step=1)


if st.button("Провери"):
    if user_answer == 8:
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор. Опитайте отново.")
