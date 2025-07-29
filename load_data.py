# Python e Sql - Pipeline de Carga de dados

# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Cria o motor de conexão (ATENÇÃO COM A STRING DE CONEXÃO ABAIXO)
#Create a connection engine (BE CAREFUL WITH THE CONNECTION STRING BELOW)
engine= create_engine('postgresql+psycopg2://rachid:admin1010@localhost:5222/database')

print("\n Iniciando o Processo de Carga dos Dados!\n")

# Função para carregar os dados csv para o PostgreSQL no schema especificado
# Function to load CSV data into PostgreSQL in the specified schema
def load_data(csv_file, table_name, schema):
    # try/except block
    try:
        # Read csv file
        df = pd.read_csv(csv_file)

        # Execute sql using Pandas dataframe
        df.to_sql(table_name, engine, schema=schema, if_exists='append', index=False )
        print(f"Dados do arquivo {csv_file} foram inseridos na tabela {schema}.{table_name}.")

    except Exception as e:
        print(f'Erro ao inserir dados do arquivo {csv_file} na tabela {schema}.{table_name}.')


# Carregamento dos dados no schema 'tables'
# Loading data into the 'tables' schema


load_data('data/clientes.csv','clientes','rag_analytics')
load_data('data/produtos.csv','produtos_eletronicos','rag_analytics')
load_data('data/vendas.csv','vendas', 'rag_analytics')


print("\nCarga Executada com Sucesso! Use o pgAdmin Para checar os Dados se desejar:\n")
print("\nIniciando o Processo de Análise dos dados com IA. Seja paciênte e aguarde o Excelente resultado que será entregue a você!\n")