import streamlit as st

st.write("Колко е 5 + 3?")


user_answer = st.number_input("Въведете отговора:", step=1)


if st.button("Провери"):
    if user_answer == 8:
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор. Опитайте отново.")



st.write("Коя е столицата на България?")


user_answer = st.text_input("Въведете отговора:", step=1)


if st.button("Провери"):
    if user_answer == София:
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор. Опитайте отново.")

st.write(" Къде живее илия кирилов рангелов?")
if user_answer == Асеновград:
    st.write("Верен отговор!")
else:
    st.write("Гревен отговор. Опитайте отново.)


