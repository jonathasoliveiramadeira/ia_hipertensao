import streamlit as st
import numpy as np

from components.formulario import criar_formulario
from components.resultado import mostrar_resultado
from components.calculos import calcular_imc
from utils.helpers import converter_sexo
from PIL import Image


# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================

st.set_page_config(
    page_title="IA de Hipertensão",
    page_icon="🩺",
    layout="centered"
)


# ======================================================
# CARREGAR CSS
# ======================================================

with open("app/styles/style.css", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )


# ======================================================
# CARREGAR LOGO
# ======================================================

logo = Image.open("app/assets/logo.png")

st.image(
    logo,
    width=120
)


# ======================================================
# TÍTULO
# ======================================================

st.markdown(
    '<div class="main-title">IA de Predição de Hipertensão</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">Sistema de apoio preliminar para análise de hipertensão arterial.</div>',
    unsafe_allow_html=True
)


st.divider()


# ======================================================
# FORMULÁRIO
# ======================================================

paciente = criar_formulario()


# ======================================================
# CALCULAR IMC
# ======================================================

imc = calcular_imc(
    paciente["peso"],
    paciente["altura"]
)


st.write(f"IMC calculado: {imc:.2f}")

# ======================================================
# BOTÃO DE ANÁLISE
# ======================================================

if st.button("Analisar"):

    sexo = converter_sexo(
        paciente["sexo"]
    )


    dados_paciente = np.array([
        [
            paciente["idade"],
            paciente["peso"],
            paciente["altura"],
            imc,
            sexo,
            paciente["pressao_sistolica"],
            paciente["pressao_diastolica"]
        ]
    ])


    # ==================================================
    # SIMULAÇÃO TEMPORÁRIA
    # ==================================================

    risco = 0


    if paciente["idade"] > 50:
        risco += 20

    if imc > 30:
        risco += 25

    if paciente["pressao_sistolica"] > 140:
        risco += 30

    if paciente["pressao_diastolica"] > 90:
        risco += 25


    risco = min(risco, 100)


    mostrar_resultado(risco)


# ======================================================
# RODAPÉ
# ======================================================

st.divider()

st.caption(
    "Projeto acadêmico de Inteligência Artificial aplicada à saúde."
)

# Para rodar localmente, use:
# streamlit run app/interface.py
# localhost:8501