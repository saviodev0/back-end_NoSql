from pymongo import MongoClient

uri = "mongodb+srv://meuBanco:dbSavio@cluster0.mhgaegb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)

    client.admin.command("ping")

    print(" Conectado ao MongoDB Atlas com sucesso!")

except Exception as e:
    print(" Erro ao conectar:")
    print(e)