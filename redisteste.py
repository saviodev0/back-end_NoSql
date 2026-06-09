import redis

try:
    r = redis.Redis(
        host="willing-bunny-133641.upstash.io",
        port=6379,
        password="gQAAAAAAAgoJAAIgcDFhMGVmODhhMTM5ZmI0YTZhODNmOThkZWE3MWQ1OGQ1NA",
        ssl=True,
        decode_responses=True
    )

    print("Conectando...")
    print(r.ping())

except Exception as e:
    print("Erro:")
    print(e)