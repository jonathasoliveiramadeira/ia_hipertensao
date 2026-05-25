# ======================================================
# IMPORTAÇÕES
# ======================================================

import streamlit as st


# ======================================================
# EXIBIÇÃO DO RESULTADO
# ======================================================


def mostrar_resultado(risco):

    st.divider()

    st.subheader("Resultado da Análise")


    if risco < 30:

        st.success("Baixo Risco")

    elif risco < 70:

        st.warning("Risco Moderado")

    else:

        st.error("Alto Risco")


    st.write(
        f"Probabilidade estimada de hipertensão: {risco}%"
    )


    st.info(
        "Esta análise possui caráter preliminar e não substitui avaliação médica profissional."
    )