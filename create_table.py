# Python - Pipeline de criação de banco de dados
# Os dados tem que ser fornecidos pela empresa.
# Esse script executa o aquivo sql para criar outro banco de dados a partir dos dados fornecidos pela empresa
# No nosso caso os dados fornecidos foram, "clientes.csv", "produtos.csv", "vendas.csv"
# A partir desses dados será gerado um relatório feito por um LLM


# Import 
import psycopg2
import time

# Função para executar script sql

def exe_sql_script(filename):

    # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    conn = psycopg2.connect(
        dbname="database",
        user="rachid",
        password="admin1010",
        host="localhost",
        port="5222"
    )

     # Abre um cursor para realizar operações no banco de dados
    cur = conn.cursor()
    time.sleep(3)

    # Lê o conteúdo do arquivo SQL
    with open(filename, 'r') as file:
        sql_script = file.read()

    try:
        # Executa o script SQL
        cur.execute(sql_script)

        # Confirma as mudanças no banco de dados
        conn.commit()  
        print("\nScript executado com sucesso!\n")
    except Exception as e:
        # Reverte as mudanças em caso de erro
        conn.rollback()  
        print(f"Erro ao executar o script: {e}")
    finally:
        # Fecha a comunicação com o banco de dados
        cur.close()
        conn.close()

# Executa o script sql

exe_sql_script("data/tables.sql")

