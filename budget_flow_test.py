# -*- coding: utf-8 -*-

import streamlit as st # import the streamlit library
import pandas as pd
import matplotlib.pyplot as plt

# Título do App
st.title('Budget Flow - Projeção Mensal e Anual')

# Seções do App
st.header('Insira seus Dados')

# Função para capturar os dados do usuário via Streamlit
def inserir_dados_streamlit():
    categorias = {}

    # Receitas
    st.subheader('Receitas')
    categorias["Receitas"] = {}
    n_receitas = st.number_input("Quantas fontes de receita você tem?", min_value=1, step=1)
    for i in range(n_receitas):
        fonte = st.text_input(f"Digite o nome da receita {i + 1}", key=f"receita_{i}")
        valor = st.number_input(f"Digite o valor mensal da receita {i + 1}: R$", min_value=0.0, step=100.0, key=f"valor_receita_{i}")
        categorias["Receitas"][fonte] = valor

    # Despesas Fixas
    st.subheader('Despesas Fixas')
    categorias["Despesas Fixas"] = {}
    n_despesas_fixas = st.number_input("Quantas despesas fixas você tem?", min_value=1, step=1)
    for i in range(n_despesas_fixas):
        despesa = st.text_input(f"Digite o nome da despesa fixa {i + 1}", key=f"despesa_fixa_{i}")
        valor = st.number_input(f"Digite o valor mensal da despesa fixa {i + 1}: R$", min_value=0.0, step=50.0, key=f"valor_despesa_fixa_{i}")
        categorias["Despesas Fixas"][despesa] = valor

    # Despesas Variáveis
    st.subheader('Despesas Variáveis')
    categorias["Despesas Variáveis"] = {}
    n_despesas_variaveis = st.number_input("Quantas despesas variáveis você tem?", min_value=1, step=1)
    for i in range(n_despesas_variaveis):
        despesa = st.text_input(f"Digite o nome da despesa variável {i + 1}", key=f"despesa_variavel_{i}")
        valor = st.number_input(f"Digite o valor mensal da despesa variável {i + 1}: R$", min_value=0.0, step=50.0, key=f"valor_despesa_variavel_{i}")
        categorias["Despesas Variáveis"][despesa] = valor

    # Impostos
    st.subheader('Impostos')
    categorias["Impostos"] = {}
    n_impostos = st.number_input("Quantos impostos você paga?", min_value=1, step=1)
    for i in range(n_impostos):
        imposto = st.text_input(f"Digite o nome do imposto {i + 1}", key=f"imposto_{i}")
        valor = st.number_input(f"Digite o valor mensal do imposto {i + 1}: R$", min_value=0.0, step=50.0, key=f"valor_imposto_{i}")
        categorias["Impostos"][imposto] = valor

    # Investimentos
    st.subheader('Investimentos')
    categorias["Investimentos"] = {}
    n_investimentos = st.number_input("Quantos investimentos você faz?", min_value=1, step=1)
    for i in range(n_investimentos):
        investimento = st.text_input(f"Digite o nome do investimento {i + 1}", key=f"investimento_{i}")
        valor = st.number_input(f"Digite o valor mensal do investimento {i + 1}: R$", min_value=0.0, step=50.0, key=f"valor_investimento_{i}")
        categorias["Investimentos"][investimento] = valor

    return categorias
    # Função para calcular o total de cada categoria mensal
def calcular_total_mensal(categoria):
    return sum(categorias[categoria].values())

# Função para calcular o total de cada categoria anual
def calcular_total_anual(categoria):
    return sum(categorias[categoria].values()) * 12

# Captura os dados do usuário
categorias = inserir_dados_streamlit()

# Calcular os totais por categoria (mensal e anual)
total_receitas_mensal = calcular_total_mensal("Receitas")
total_despesas_fixas_mensal = calcular_total_mensal("Despesas Fixas")
total_despesas_variaveis_mensal = calcular_total_mensal("Despesas Variáveis")
total_impostos_mensal = calcular_total_mensal("Impostos")
total_investimentos_mensal = calcular_total_mensal("Investimentos")

total_receitas_anual = calcular_total_anual("Receitas")
total_despesas_fixas_anual = calcular_total_anual("Despesas Fixas")
total_despesas_variaveis_anual = calcular_total_anual("Despesas Variáveis")
total_impostos_anual = calcular_total_anual("Impostos")
total_investimentos_anual = calcular_total_anual("Investimentos")

# Calcular o fluxo de caixa mensal e anual
fluxo_caixa_mensal = total_receitas_mensal - (total_despesas_fixas_mensal + total_despesas_variaveis_mensal + total_impostos_mensal + total_investimentos_mensal)
fluxo_caixa_anual = total_receitas_anual - (total_despesas_fixas_anual + total_despesas_variaveis_anual + total_impostos_anual + total_investimentos_anual)

# Exibir o resumo dos resultados
st.header('Resumo do Orçamento')
st.write(f"Receitas Mensais: R$ {total_receitas_mensal}")
st.write(f"Receitas Anuais: R$ {total_receitas_anual}")
st.write(f"Despesas Fixas Mensais: R$ {total_despesas_fixas_mensal}")
st.write(f"Despesas Fixas Anuais: R$ {total_despesas_fixas_anual}")
st.write(f"Despesas Variáveis Mensais: R$ {total_despesas_variaveis_mensal}")
st.write(f"Despesas Variáveis Anuais: R$ {total_despesas_variaveis_anual}")
st.write(f"Impostos Mensais: R$ {total_impostos_mensal}")
st.write(f"Impostos Anuais: R$ {total_impostos_anual}")
st.write(f"Investimentos Mensais: R$ {total_investimentos_mensal}")
st.write(f"Investimentos Anuais: R$ {total_investimentos_anual}")
st.write(f"Fluxo de Caixa Mensal: R$ {fluxo_caixa_mensal}")
st.write(f"Fluxo de Caixa Anual: R$ {fluxo_caixa_anual}")

# Visualizar os gráficos de despesas mensais e anuais
st.subheader('Visualização Gráfica')

categorias_gastos = ["Despesas Fixas", "Despesas Variáveis", "Impostos", "Investimentos"]
valores_gastos_mensal = [total_despesas_fixas_mensal, total_despesas_variaveis_mensal, total_impostos_mensal, total_investimentos_mensal]
valores_gastos_anual = [total_despesas_fixas_anual, total_despesas_variaveis_anual, total_impostos_anual, total_investimentos_anual]

# Gráfico de barras para despesas mensais
st.write("Distribuição das Despesas Mensais")
fig, ax = plt.subplots()
ax.bar(categorias_gastos, valores_gastos_mensal, color="lightcoral")
ax.set_ylabel("Valor em R$")
st.pyplot(fig)

# Gráfico de barras para despesas anuais
st.write("Distribuição das Despesas Anuais")
fig, ax = plt.subplots()
ax.bar(categorias_gastos, valores_gastos_anual, color="skyblue")
ax.set_ylabel("Valor em R$")
st.pyplot(fig)
