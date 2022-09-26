import random

proxies_pool = [
    {'http': '118.24.249:1231'},
    {'http': '115.12.121:123'},
]

proxies = random.choice(proxies_pool)

print(proxies)
