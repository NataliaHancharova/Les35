import requests
import time
import multiprocessing

def processes(url):
    return requests.get(url)

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        urls = ['https://www.example.com','https://www.21vek.by','https://www.onliner.by']
        print('Выполнение процесса')
        start = time.time()
        results = pool.map(processes, urls)
        
    end = time.time()
    print('Последовательные результаты:', results)
    print('Время выполнения в сек:', end - start)