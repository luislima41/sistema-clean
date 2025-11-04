Sistema Refatorado (Clean Architecture)

Este repositório contém a versão refatorada do sistema legado originalmente desenvolvido em MVC, transformada para o padrão Clean Architecture com suporte de um modelo de linguagem (LLM) e técnicas de Inteligência Artificial.

Contexto

O sistema foi gerado automaticamente a partir do repositório mvc-legacy-system utilizando o script disponível em auto-refactor-script.
O objetivo da transformação foi:

Melhorar modularidade e testabilidade;

Isolar regras de negócio da infraestrutura;

Promover arquitetura independente de frameworks.

Estrutura do Projeto

clean-architecture-system/
├── domain/
├── usecases/
├── infrastructure/
├── interfaces/
└── README.md

Requisitos

Python 3.10+

Flask ou FastAPI (dependendo da camada de interface)

pytest (para execução de testes unitários)

Execução

Instalar dependências:

pip install -r requirements.txt


Rodar aplicação:

python main.py

Testes

Para executar os testes:

pytest"# sistema-clean" 
