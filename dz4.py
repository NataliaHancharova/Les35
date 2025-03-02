import math
import time
import multiprocessing


def calculate_sqrt_sum(number):
    sum = 0.0
    for i in range(1, number+1):
        sum += math.sqrt(i)
    return sum

def main():
    numbers = [12365698, 14254236, 4785699, 4522542]
    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sqrt_sum, numbers)

    end = time.time()
    print('Потоковые результаты: ', results)   
    print('Время выполнения в сек : ', end - start)

if __name__ == "__main__":
    main()