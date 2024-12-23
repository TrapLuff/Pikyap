import random
# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    result = [random.randint(begin,end) for _ in range(num_count)]
    return result

if __name__ == '__main__':
    print(gen_random(5, 1, 3))