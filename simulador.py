import streamlit as st

st.set_page_config(page_title="Simulador de Decisão", layout="centered")

# ------------------------
# ESTILO (CSS)
# ------------------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    color: #aaa;
    margin-bottom: 20px;
}
.button-main button {
    background-color: #4A90E2;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}
.card {
    padding: 20px;
    border-radius: 16px;
    border: 2px solid #4A90E2;
    text-align: center;
    font-size: 20px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# FUNÇÃO DE DECISÃO
# ------------------------
def calcular(opcao, custo, prazo, risco):
    score = 0
    explicacao = []

    if custo == "baixo":
        score += 3
        explicacao.append("✔ Custo baixo (+3)")
    else:
        score -= 2
        explicacao.append("✖ Custo alto (-2)")

    if prazo == "curto":
        score += 2
        explicacao.append("✔ Prazo curto (+2)")

    if risco == "alto":
        score -= 1
        explicacao.append("✖ Risco alto (-1)")

    return score, explicacao


# ------------------------
# ESTADO
# ------------------------
if "resultado" not in st.session_state:
    st.session_state.resultado = None


# ------------------------
# TELA 1
# ------------------------
if st.session_state.resultado is None:

    st.markdown('<div class="big-title">🧠 Simulador de Decisão ☕</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Me conte o que precisa decidir</div>', unsafe_allow_html=True)

    problema = st.text_area("Descrição", placeholder="Ex: mudar de emprego...")

    st.subheader("Opções")
    opcao1 = st.text_input("Opção 1")
    opcao2 = st.text_input("Opção 2")

    st.subheader("Critérios")
    custo = st.selectbox("Custo", ["baixo", "alto"])
    prazo = st.selectbox("Prazo", ["curto", "longo"])
    risco = st.selectbox("Risco", ["baixo", "alto"])

    st.markdown('<div class="button-main">', unsafe_allow_html=True)
    if st.button("Simular decisão"):
        s1, e1 = calcular(opcao1, custo, prazo, risco)
        s2, e2 = calcular(opcao2, custo, prazo, risco)

        if s1 > s2:
            st.session_state.resultado = (opcao1, e1)
        else:
            st.session_state.resultado = (opcao2, e2)

        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ------------------------
# TELA 2
# ------------------------
else:
    decisao, explicacao = st.session_state.resultado

    st.markdown('<div class="big-title">📊 Resultado</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="card">Decisão sugerida:<br><b>{decisao}</b></div>', unsafe_allow_html=True)

    st.subheader("Como chegamos aqui?")
    for item in explicacao:
        st.write(item)

    if st.button("Refazer simulação"):
        st.session_state.resultado = None
        st.rerun()