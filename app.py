import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador Brasileirão 2026 - By Charles Borges", page_icon="⚽", layout="centered")

st.title("🏆 Simulador do Título - Brasileirão 2026 - By Charles Borges")
st.markdown("Simule os resultados das últimas rodadas e veja quem leva a taça entre **Flamengo** e **Palmeiras**!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 Flamengo (73 pts)")
    f_r34 = st.selectbox("34ª vs Grêmio", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    f_r35 = st.selectbox("35ª vs Athletico-PR", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    f_r36 = st.selectbox("36ª vs Palmeiras (Clássico)", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=1)[1]
    f_r37 = st.selectbox("37ª vs Coritiba", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    f_r38 = st.selectbox("38ª vs Chapecoense", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]

# Lógica espelhada para o clássico da 36ª rodada
if f_r36 == 3:
    p_r36 = 0
elif f_r36 == 0:
    p_r36 = 3
else:
    p_r36 = 1

with col2:
    st.markdown("### 🟢 Palmeiras (70 pts)")
    p_r34 = st.selectbox("34ª vs Remo", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    p_r35 = st.selectbox("35ª vs Cruzeiro", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    
    clássico_texto = "Vitória (3 pts)" if p_r36==3 else ("Empate (1 pt)" if p_r36==1 else "Derrota (0 pts)")
    st.text_input("36ª vs Flamengo (Clássico)", value=clássico_texto, disabled=True)
    
    p_r37 = st.selectbox("37ª vs Chapecoense", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]
    p_r38 = st.selectbox("38ª vs Coritiba", [("Vitória (3 pts)", 3), ("Empate (1 pt)", 1), ("Derrota (0 pts)", 0)], format_func=lambda x: x[0], index=0)[1]

# Cálculo final
p_fla = 73 + f_r34 + f_r35 + f_r36 + f_r37 + f_r38
p_pal = 70 + p_r34 + p_r35 + p_r36 + p_r37 + p_r38

st.divider()
st.subheader("📊 Resultado da Simulação")

col_res1, col_res2 = st.columns(2)
col_res1.metric(label="Flamengo", value=f"{p_fla} pts")
col_res2.metric(label="Palmeiras", value=f"{p_pal} pts")

if p_fla > p_pal:
    st.success(f"🏆 **Flamengo Campeão!** Abre {p_fla - p_pal} ponto(s) de vantagem.")
elif p_pal > p_fla:
    st.success(f"🏆 **Palmeiras Campeão!** Abre {p_pal - p_fla} ponto(s) de vantagem.")
else:
    st.warning("⚖️ **Empate em pontos!** O título será decidido nos critérios de desempate (vitórias/saldo).")

# Gráfico
fig, ax = plt.subplots(figsize=(6, 3))
times = ['Flamengo', 'Palmeiras']
pontos = [p_fla, p_pal]
cores = ['#dc2626', '#16a34a']

bars = ax.bar(times, pontos, color=cores, width=0.4)
ax.set_ylabel('Pontuação Total')
ax.set_ylim(70, 95)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval} pts', ha='center', va='bottom', fontweight='bold')

st.pyplot(fig)
