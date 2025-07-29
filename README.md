
# (Nome do Projeto)

## Descrição
Este projeto implementa um **sistema RAG (Retrieval-Augmented Generation)** utilizando o modelo **LLaMA 3.1** para realizar análises detalhadas de clientes, produtos e vendas.  
O modelo é orientado por um prompt que assume o papel de um **analista especializado**, retornando feedbacks e sugestões com base em informações armazenadas no banco de dados temporário.

A execução é automatizada: o pipeline cria um container Docker, popula as tabelas com dados CSV, realiza a análise via LLaMA 3.1 e, ao final, destrói todo o ambiente, gerando um arquivo final **`llm_analysis.csv`**.

---

## Funcionalidades
- Integração com **LLaMA 3.1** para análise contextual.  
- Pipeline completo com:
  1. Criação do banco de dados via **tables.sql**.
  2. Importação dos arquivos CSV:
     - `clientes.csv`
     - `produtos.csv`
     - `vendas.csv`
  3. Execução da análise e geração do relatório.
  4. Destruição automática do container.
- Resultado final exportado em **CSV**.

---

## Pré-requisitos
- **Python 3.10+**  
- **Docker**  
- **Modelo LLaMA 3.1** configurado e acessível.

---



---

## Como usar
1. Certifique-se de ter o Docker e o LLaMA 3.1 rodando corretamente.  
2. Navegue até a pasta raiz do projeto:  
   ```bash
   cd caminho/para/o/projeto
   ```
3. Execute o pipeline:  
   ```bash
   python exe_pipeline.py
   ```
4. O resultado será gerado no arquivo:  
   ```
   llm_analysis.csv
   ```

---

## Estrutura do Projeto
```
.
├── data/
│   ├── clientes.csv
│   ├── produtos.csv
│   ├── vendas.csv
│   └── tables.sql
├── exe_pipeline.py
├── requirements.txt
├── README.md
└── ...
```

---

## Status do Projeto
> **Em desenvolvimento**

---


