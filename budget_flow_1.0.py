# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CWLaZ1m2KZL8gRubGkJ55bOgmEo4-e5V
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Função para gerar dados de exemplo para cada mês
def gerar_dados_exemplo():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dados = {mes: {
        "Receitas": 0.0, 
        "Despesas": 0.0, 
        "Investimentos": 0.0,
        "Orcamento Planejado": 0.0
        } for mes in meses}
    return dados

# Inicializar os dados no session_state se ainda não estiverem definidos
if 'dados_por_mes' not in st.session_state:
    st.session_state.dados_por_mes = gerar_dados_exemplo()

# Função para exibir o resumo de um mês com estilo futurístico
def exibir_resumo_mes(mes, dados_mes):
    receitas = dados_mes['Receitas']
    despesas = dados_mes['Despesas']
    investimento = dados_mes['Investimentos']
    orcamento_planejado = dados_mes['Orcamento Planejado']
    
    # Verificar se as despesas estão acima das receitas e alertar
    if despesas > receitas:
        st.error(f"Atenção! As despesas estão acima das receitas em {mes}.")
    elif despesas > orcamento_planejado:
        st.warning(f"Atenção! As despesas ultrapassaram o orçamento planejado para {mes}.")
    
    st.markdown(f"""
    <div style='background-color:#1e1e2e; padding:20px; border-radius:15px; margin-bottom:10px; color:#fff;'>
        <h4 style='text-align:center;'>{mes} 2023</h4>
        <p><b>Receitas:</b> R$ {receitas:.2f}</p>
        <p><b>Despesas:</b> R$ {despesas:.2f}</p>
        <p><b>Investimentos:</b> R$ {investimento:.2f}</p>
        <p><b>Orçamento Planejado:</b> R$ {orcamento_planejado:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

# Função para calcular a distribuição em porcentagens
def calcular_percentuais(dados_mes):
    try:
        total = dados_mes['Receitas'] + dados_mes['Despesas'] + dados_mes['Investimentos']
        if total == 0:
            return [0, 0, 0]
        percent_receitas = (dados_mes['Receitas'] / total) * 100
        percent_despesas = (dados_mes['Despesas'] / total) * 100
        percent_investimentos = (dados_mes['Investimentos'] / total) * 100
        return [percent_receitas, percent_despesas, percent_investimentos]
    except:
        return [0, 0, 0]

# Função para gerar recomendações com base no controle financeiro
def gerar_recomendacoes(mes, dados_mes):
    receitas = dados_mes['Receitas']
    despesas = dados_mes['Despesas']
    investimento = dados_mes['Investimentos']
    orcamento_planejado = dados_mes['Orcamento Planejado']

    if despesas > receitas:
        st.write(f"**Recomendação para {mes}:** As despesas estão acima das receitas. Tente reduzir suas despesas para equilibrar seu orçamento.")
    elif despesas > orcamento_planejado:
        excesso = despesas - orcamento_planejado
        st.write(f"**Recomendação para {mes}:** As despesas ultrapassaram o orçamento planejado por R$ {excesso:.2f}. Tente ajustar seus custos para manter o controle financeiro.")

# Função para gerar o gráfico de pizza
def gerar_grafico_pizza(mes):
    dados_mes = st.session_state.dados_por_mes[mes]
    percentuais = calcular_percentuais(dados_mes)
    df_percent = pd.DataFrame({
        'Categoria': ['Receitas', 'Despesas', 'Investimentos'],
        'Percentual': percentuais
    })
    fig = px.pie(df_percent, values='Percentual', names='Categoria', title=f'Distribuição em {mes}')
    st.plotly_chart(fig)

# Função para gerar o gráfico anual de linha
def gerar_grafico_anual():
    resumo = {"Meses": [], "Receitas": [], "Despesas": []}
    for mes, dados in st.session_state.dados_por_mes.items():
        resumo['Meses'].append(mes)
        resumo['Receitas'].append(dados['Receitas'])
        resumo['Despesas'].append(dados['Despesas'])
    
    df_resumo = pd.DataFrame(resumo)
    fig = px.line(df_resumo, x='Meses', y=['Receitas', 'Despesas'], title="Evolução Anual de Receitas e Despesas")
    st.plotly_chart(fig)

# Página inicial
st.title('Planejamento Financeiro - Meses do Ano')

# Layout futurístico para Resumo dos Meses
st.markdown('---')
st.markdown('<h2 style="text-align:center; color:#42b883;">Resumo dos Meses</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
meses = list(st.session_state.dados_por_mes.keys())

for i, mes in enumerate(meses):
    col = [col1, col2, col3][i % 3]  # Distribuir os meses entre as colunas
    with col:
        exibir_resumo_mes(mes, st.session_state.dados_por_mes[mes])

# Seção de edição de Receitas e Despesas com caixa expansível após seleção do mês
st.markdown('---')
st.markdown('<h2 style="text-align:center; color:#42b883;">Editar Receitas e Despesas</h2>', unsafe_allow_html=True)

mes_selecionado = st.selectbox("Selecione o mês para editar", meses)

# Caixa expansível para editar dados do mês selecionado
with st.expander(f"Editar {mes_selecionado}"):
    st.session_state.dados_por_mes[mes_selecionado]['Receitas'] = st.number_input(f"Receitas em {mes_selecionado}", min_value=0.0, step=100.0, value=st.session_state.dados_por_mes[mes_selecionado]['Receitas'])
    st.session_state.dados_por_mes[mes_selecionado]['Despesas'] = st.number_input(f"Despesas em {mes_selecionado}", min_value=0.0, step=100.0, value=st.session_state.dados_por_mes[mes_selecionado]['Despesas'])
    st.session_state.dados_por_mes[mes_selecionado]['Investimentos'] = st.number_input(f"Investimentos em {mes_selecionado}", min_value=0.0, step=100.0, value=st.session_state.dados_por_mes[mes_selecionado]['Investimentos'])
    st.session_state.dados_por_mes[mes_selecionado]['Orcamento Planejado'] = st.number_input(f"Orçamento Planejado para {mes_selecionado}", min_value=0.0, step=100.0, value=st.session_state.dados_por_mes[mes_selecionado]['Orcamento Planejado'])

# Mostrar recomendações após edição
st.markdown('---')
st.markdown(f"### Recomendações para {mes_selecionado}")
gerar_recomendacoes(mes_selecionado, st.session_state.dados_por_mes[mes_selecionado])

# Gráfico de Pizza
st.markdown('---')
st.subheader('Gráfico de Pizza (Selecione o Mês)')
gerar_grafico_pizza(mes_selecionado)

# Gráfico Anual de Linha
st.markdown('---')
st.subheader('Gráfico Anual de Linha')
gerar_grafico_anual()
