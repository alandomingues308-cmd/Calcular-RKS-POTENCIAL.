import streamlit as st

st.title("Calculadora RKS / Potencial")

modo = st.radio("Elige juego:", ["Phigros", "Arcaea"], horizontal=True)

def constante_arcaea(score):
    if score >= 10_000_000:
        return 2.0
    elif score >= 9_800_000:
        return 1.0 + (score - 9_800_000) / 200_000
    else:
        return (score - 9_500_000) / 300_000

if modo == "Phigros":
    with st.form("phigros_form"):
        precision = st.number_input("Precisión %", min_value=0.0, max_value=100.0, step=0.01)
        dificultad = st.number_input("Dificultad", min_value=0.0, step=0.1)
        calcular = st.form_submit_button("Calcular")
    
    if calcular:
        rks = 0 if precision < 55 else ((precision - 55) / 45) ** 2 * dificultad
        st.success(f"tu rks es igual a {rks:.3f}")

if modo == "Arcaea":
    with st.form("arcaea_form"):
        score = st.number_input("Puntaje", min_value=0, max_value=10_000_000, step=1000)
        dificultad = st.number_input("Dificultad", min_value=0.0, step=0.1)
        calcular = st.form_submit_button("Calcular")
    
    if calcular:
        potencial = dificultad + constante_arcaea(score)
        st.success(f"tu rks es igual a {potencial:.2f}")
        