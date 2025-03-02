import math
import time

def calculate_sqrt_sum(number):
    sum = 0.0
    for i in range(1, number+1):
        sum += math.sqrt(i)
    return sum

def main():
    numbers = [1000000, 12365698, 14254236, 4785699, 4522542]
    results = [] 
    start = time.time()
    for number in numbers:
        results.append(calculate_sqrt_sum(number))
    end = time.time()
    print('Последовательные результаты: ', results)   
    print('Время выполнения в сек :', end - start)

if __name__ == "__main__":
    main()
