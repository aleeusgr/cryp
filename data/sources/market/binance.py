
def read_key(file = 'binance'):
    key = {}
    with open(f'./data/keys/{file}') as f:
        content = f.read().splitlines()
        for i in content:
            x = i.split(sep = ': ')
            key[x[0]] = x[1]
    return key


def auth():
    key = read_key()

    from binance.client import Client
    api_key,api_secret = (i for i in key.values())

    client = Client(api_key, api_secret)
    
    return client

