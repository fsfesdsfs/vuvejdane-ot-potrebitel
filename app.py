import streamlit as st

st.write("Колко е 5 + 3?")
q1 = st.number_input("Отговор 1:", step=1)
if st.button("Провери 1"):
    if q1 == 8:
        st.write("✅ Верен отговор!")
    else:
        st.write("❌ Грешен отговор.")

st.write("Коя е столицата на България?")
q2 = st.text_input("Отговор 2:")
if st.button("Провери 2"):
    if q2.lower() == "софия":
        st.write("✅ Верен отговор!")
    else:
        st.write("❌ Грешен отговор.")

st.write("Колко е 9 - 4?")
q3 = st.number_input("Отговор 3:", step=1)
if st.button("Провери 3"):
    if q3 == 5:
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор.")

st.write("Колко е 6 × 2?")
q4 = st.number_input("Отговор 4:", step=1)
if st.button("Провери 4"):
    if q4 == 12:
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор.")

st.write("На кой континент се намира България?")
q5 = st.text_input("Отговор 5:")
if st.button("Провери 5"):
    if q5.lower() == "европа":
        st.write(" Верен отговор!")
    else:
        st.write(" Грешен отговор.")
