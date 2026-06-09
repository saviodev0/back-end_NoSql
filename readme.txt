🚀 Integração MongoDB + Redis com Python

Projeto de exemplo utilizando MongoDB e Redis com Python, demonstrando:

Conexão com MongoDB
CRUD completo no MongoDB
Operações básicas no Redis
Cache Redis integrado ao MongoDB
Uso de variáveis de ambiente com .env
📚 Tecnologias utilizadas
Python 3
MongoDB
Redis
PyMongo
Redis-py
python-dotenv
📦 Instalação
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio
2. Crie o ambiente virtual
Windows
python -m venv venv

venv\Scripts\activate
Linux / Mac
python3 -m venv venv

source venv/bin/activate
3. Instale as dependências
pip install -r requirements.txt
📄 Arquivo requirements.txt

Crie um arquivo chamado requirements.txt:

pymongo
redis
python-dotenv
⚙️ Configuração do arquivo .env

Crie um arquivo .env na raiz do projeto:

MONGO_URI=sua_uri_mongodb

REDIS_HOST=seu_host_redis
REDIS_PORT=6379
REDIS_PASSWORD=sua_senha_redis
▶️ Executando o projeto
python main.py
🧠 Funcionalidades
MongoDB

O projeto executa:

Inserção de produtos
Consulta de produtos
Atualização de dados
Remoção de registros
Exemplo de documento:
{
  "nome": "Notebook",
  "preco": 3500,
  "categoria": "Eletronicos"
}
Redis

O projeto demonstra:

String
SET mensagem:inicio
GET mensagem:inicio
Hash
HSET usuario:1
HGETALL usuario:1
Lista
RPUSH logs
LRANGE logs
⚡ Cache Redis + MongoDB

A função buscar_produto() utiliza:

Busca no Redis
Caso não exista:
consulta no MongoDB
armazena no Redis
define expiração de 60 segundos

Fluxo:

Redis Cache → MongoDB → Redis Cache
📂 Estrutura do projeto
.
├── main.py
├── .env
├── requirements.txt
└── README.md
🛠 Exemplo de saída
Conectado ao MongoDB
Conectado ao Redis

===== CRUD MONGODB =====

Produtos inseridos

===== CACHE REDIS + MONGODB =====

Primeira busca:
Produto encontrado no MongoDB e armazenado no cache por 60 segundos

Segunda busca:
Produto encontrado no cache Redis
📌 Objetivo do projeto

Este projeto foi criado para praticar conceitos de:

Banco de dados NoSQL
Cache com Redis
Integração entre serviços
CRUD com MongoDB
Variáveis de ambiente
Python backend
👨‍💻 Autor

Desenvolvido por Sávio Junior Coelho de Carvalho
