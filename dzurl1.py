import time
import requests

def get_url():
    urls = ['https://www.example.com','https://www.21vek.by','https://www.onliner.by']
    start = time.time()
    for url in urls:
        requests.get(url)

    end = time.time()
    print(f'Выполнилось за {end - start} секунд')

get_url()