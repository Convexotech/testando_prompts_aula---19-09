import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="App Simples no Render", page_icon="🚀", layout="wide"
)

# Título da aplicação
st.title("🚀 Meu App Streamlit no Render")
st.write(
    "Esta é uma aplicação simplificada em **arquivo único** pronta para deploy."
)

# Sidebar para navegação ou controles
st.sidebar.header("Painel de Controle")
opcao = st.sidebar.selectbox(
    "Escolha a funcionalidade", ["Gerador de Dados (Exemplo)", "Upload de CSV"]
)

if opcao == "Gerador de Dados (Exemplo)":
    st.subheader("📊 Visualização de Dados de Exemplo")

    # Criando dados fictícios
    df = pd.DataFrame(
        {
            "Categoria": ["A", "B", "C", "D", "E"],
            "Vendas": [120, 300, 250, 400, 180],
            "Lucro": [45, 120, 90, 160, 70],
        }
    )

    st.dataframe(df, use_container_width=True)

    # Gráfico simples
    st.bar_chart(df.set_index("Categoria"))

else:
    st.subheader("📁 Envie seu próprio arquivo CSV")
    arquivo = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

    if arquivo is not None:
        df_usuario = pd.read_csv(arquivo)
        st.success("Arquivo carregado com sucesso!")
        st.dataframe(df_usuario, use_container_width=True)

        # Estatísticas básicas
        st.subheader("📈 Estatísticas Descritivas")
        st.write(df_usuario.describe())
    else:
        st.info("Aguardando o upload de um arquivo para exibir os dados.")