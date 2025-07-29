# Python - Executa Pipelines

# Imports
import subprocess
import time

# Função para executar comandos de terminal
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"\nComando '{command}' executado com sucesso.")
        print("\nSaída:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\nErro ao executar o comando '{command}'.")
        print("\nErro:\n", e.stderr)

# Função para executar outros scripts Python
def execute_pipeline(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
        print(f"\nScript {script_name} executado com sucesso.")
        print("\nSaída:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\nErro ao executar o script {script_name}.")
        print("\nErro:\n", e.stderr)



# Comandos para criação do container Docker e instalação dos pacotes
docker_command = "docker run --name rag_analysis -p 5222:5432 -e POSTGRES_USER=rachid -e POSTGRES_PASSWORD=admin1010 -e POSTGRES_DB=database -d postgres:16.1"
time.sleep(0.5)
pip_command = "pip install -r requirements.txt"

# Inicia um timer
start_time = time.time()

# Executa os comandos de terminal 
execute_command(docker_command)
execute_command(pip_command)


# Lista de scripts
scripts = [
    'create_table.py',
    'load_data.py',
    'exe_llm.py'
]

# Executa os scripts em um loop
for script in scripts:
    print(f'Executando o scrips {script}')
    execute_pipeline(script)
    time.sleep(0.9)
    
# Comando para destruir o container Docker
destroy_docker_command = "docker rm -f rag_analysis"
execute_command(destroy_docker_command)

# Calcula o tempo total de execução
end_time = time.time()
total_time = end_time - start_time

print(f"\nPipeline executado com sucesso.")
print(f"Tempo total de execução: {total_time:.2f} segundos.\n")
print(f"\nObrigado.\n")
