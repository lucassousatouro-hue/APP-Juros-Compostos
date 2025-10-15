import streamlit as st
import pandas as pd

st.title("💰 Calculadora de Juros Compostos")
st.write("Simule o crescimento do seu investimento mês a mês.")

# Entradas do usuário
aporte_inicial = st.number_input("Aporte inicial (R$):", min_value=0.0, value=0.0)
aporte_mensal = st.number_input("Aporte mensal (R$):", min_value=0.0, value=0.0)
taxa = st.number_input("Rendimento mensal (%):", min_value=0.0, value=1.0)
meses = st.number_input("Período (em meses, 1 a 180):", min_value=1, max_value=180, value=12)

if st.button("Calcular"):
    saldo = aporte_inicial
    taxa_decimal = taxa / 100
    evolucao = []

    for mes in range(1, meses + 1):
        juros = saldo * taxa_decimal
        saldo += juros + aporte_mensal
        evolucao.append({
            "Mês": mes,
            "Aporte": aporte_mensal if mes > 1 or aporte_inicial == 0 else aporte_inicial,
            "Juros": round(juros, 2),
            "Saldo Total": round(saldo, 2)
        })

    df = pd.DataFrame(evolucao)

    # Exibe tabela
    st.subheader("📊 Evolução mês a mês")
    st.dataframe(df)

    # Exibe resultados finais
    total_aportes = aporte_inicial + (aporte_mensal * meses)
    total_juros = saldo - total_aportes

    st.subheader("📈 Resultado final")
    st.write(f"**Total investido:** R$ {total_aportes:,.2f}")
    st.write(f"**Total de juros:** R$ {total_juros:,.2f}")
    st.write(f"**Valor final:** R$ {saldo:,.2f}")
