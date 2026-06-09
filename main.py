from dotenv import load_dotenv
import os
import json
from datetime import datetime

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import redis

# ==========================================
# CARREGAR VARIÁVEIS DE AMBIENTE
# ==========================================

load_dotenv()
print("MONGO_URI =", os.getenv("MONGO_URI"))

MONGO_URI = os.getenv("MONGO_URI")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

# ==========================================
# CONEXÃO MONGODB
# ==========================================

def conectar_mongodb():
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command("ping")
        print(" Conectado ao MongoDB")
        return client

    except ConnectionFailure as e:
        print(f" Erro de conexão MongoDB: {e}")

    except OperationFailure as e:
        print(f" Erro de autenticação MongoDB: {e}")

    return None


# ==========================================
# CONEXÃO REDIS
# ==========================================

def conectar_redis():
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            decode_responses=True,
            ssl=True
        )

        client.ping()

        print(" Conectado ao Redis")
        return client

    except redis.AuthenticationError as e:
        print(f" Erro de autenticação Redis: {e}")

    except redis.ConnectionError as e:
        print(f" Erro de conexão Redis: {e}")

    return None


# ==========================================
# OPERAÇÕES MONGODB
# ==========================================

def inserir_produtos(collection):

    produtos = [
        {
            "nome": "Notebook",
            "preco": 3500,
            "categoria": "Eletronicos"
        },
        {
            "nome": "Mouse",
            "preco": 80,
            "categoria": "Perifericos"
        },
        {
            "nome": "Caderno",
            "preco": 8,
            "categoria": "Papelaria"
        }
    ]

    collection.insert_many(produtos)

    print(" Produtos inseridos")


def consultar_produtos(collection):

    print("\nProdutos com preço maior que 10:")

    produtos = collection.find(
        {"preco": {"$gt": 10}}
    )

    for produto in produtos:
        print(produto)


def atualizar_produto(collection):

    resultado = collection.update_one(
        {"nome": "Mouse"},
        {"$set": {"preco": 99.90}}
    )

    print(
        f" Produtos atualizados: {resultado.modified_count}"
    )


def remover_produto(collection):

    resultado = collection.delete_one(
        {"categoria": "Papelaria"}
    )

    print(
        f" Produtos removidos: {resultado.deleted_count}"
    )


# ==========================================
# OPERAÇÕES REDIS
# ==========================================

def redis_string(redis_client):

    redis_client.set(
        "mensagem:inicio",
        "Bem-vindo ao desafio NoSQL!"
    )

    mensagem = redis_client.get(
        "mensagem:inicio"
    )

    print("\nMensagem:")
    print(mensagem)


def redis_hash(redis_client):

    redis_client.hset(
        "usuario:1",
        mapping={
            "nome": "João Silva",
            "email": "joao@email.com"
        }
    )

    usuario = redis_client.hgetall(
        "usuario:1"
    )

    print("\nUsuário:")
    print(usuario)


def redis_lista(redis_client):

    redis_client.rpush(
        "logs",
        f"{datetime.now()} - LOGIN"
    )

    redis_client.rpush(
        "logs",
        f"{datetime.now()} - CONSULTA_PRODUTO"
    )

    logs = redis_client.lrange(
        "logs",
        0,
        -1
    )

    print("\nLogs de acesso:")

    for log in logs:
        print(log)


# ==========================================
# CACHE REDIS + MONGODB
# ==========================================

def buscar_produto(nome, collection, redis_client):

    chave = f"produto:{nome}"

    cache = redis_client.get(chave)

    if cache:
        print("\n Produto encontrado no cache Redis")
        return json.loads(cache)

    produto = collection.find_one(
        {"nome": nome},
        {"_id": 0}
    )

    if produto:

        redis_client.set(
             chave,
            json.dumps(produto),
            ex=60
        )

        print(
            "\n Produto encontrado no MongoDB e armazenado no cache por 60 segundos"
        )

    return produto


# ==========================================
# MAIN
# ==========================================

def main():

    mongo_client = conectar_mongodb()
    redis_client = conectar_redis()

    if not mongo_client or not redis_client:
        return

    db = mongo_client["desafio_nosql"]
    collection = db["produtos"]

    # Limpa dados antigos para facilitar os testes
    collection.delete_many({})

    print("\n===== CRUD MONGODB =====")

    inserir_produtos(collection)

    consultar_produtos(collection)

    atualizar_produto(collection)

    remover_produto(collection)

    print("\n===== OPERAÇÕES REDIS =====")

    redis_string(redis_client)

    redis_hash(redis_client)

    redis_lista(redis_client)

    print("\n===== CACHE REDIS + MONGODB =====")

    print("\nPrimeira busca:")
    print(
        buscar_produto(
            "Notebook",
            collection,
            redis_client
        )
    )

    print("\nSegunda busca:")
    print(
        buscar_produto(
            "Notebook",
            collection,
            redis_client
        )
    )


if __name__ == "__main__":
    main()