# ======================================================
# IMPORTAÇÕES
# ======================================================

import streamlit as st


# ======================================================
# FORMULÁRIO DO PACIENTE
# ======================================================


def criar_formulario():

    st.subheader("Dados do Paciente")


    idade = st.number_input(
        "Idade",
        min_value=1,
        max_value=120,
        value=30
    )


    peso = st.number_input(
        "Peso (kg)",
        min_value=1.0,
        max_value=300.0,
        value=70.0
    )


    altura = st.number_input(
        "Altura (m)",
        min_value=0.50,
        max_value=2.50,
        value=1.70
    )


    sexo = st.radio(
        "Sexo",
        ["Masculino", "Feminino"]
    )


    pressao_sistolica = st.number_input(
        "Pressão Sistólica (mmHg)",
        min_value=50,
        max_value=300,
        value=120
    )


    pressao_diastolica = st.number_input(
        "Pressão Diastólica (mmHg)",
        min_value=30,
        max_value=200,
        value=80
    )


    return {
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "sexo": sexo,
        "pressao_sistolica": pressao_sistolica,
        "pressao_diastolica": pressao_diastolica
    }