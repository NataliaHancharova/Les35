import time
import requests
import threading

def get_url_1_thread():
    print('Выполняется 1 поток')
    urls = ['https://www.example.com','https://www.21vek.by','https://www.onliner.by']
    start = time.time()
    for url in urls:
        requests.get(url)


def get_url_2_thread():
    print('Выполняется 2 поток')
    urls = ['https://www.example.com','https://www.21vek.by','https://www.onliner.by']
    start = time.time()
    for url in urls:
        requests.get(url)

start = time.time()

thread_1 = threading.Thread(target=get_url_1_thread)
thread_2 = threading.Thread(target=get_url_2_thread)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end = time.time()

print(f'Время выполнения {end - start} секунд')