from datetime import datetime
from tqdm import tqdm
import os

f = 'Numbers.txt'
line = []

if os.stat(f).st_size == 0:
    line = None
else:
    with open(f) as file:
        file_1 = file.read().split(' ')
        file_ = file_1.split('\n')
    line = [int(item) for item in file_]

start_time = datetime.now()

def _at_all(line):
    if line is None:
        return None
    else:
        return len(line)


def _min(line):
    if line is None:
        return None
    else:
        _mn = min(line)
        return _mn


def _max(line):
    if line is None:
        return None
    else:
        _mx = max(line)
        return _mx


def _sum(line):
    if line is None:
        return None
    else:
        _sm = sum(line)
        return _sm


def _mult(line):
    if line is None:
        return None
    else:
        _mult = 1
        for i in tqdm(line):
            _mult = (_mult * i)
        return _mult


def _delimost(line):
    if line is None:
        return None
    else:
        _sum = sum(line)
        _del = _sum % 3
        return _del


print("Количество чисел:", _at_all(line))
print("Минимальное значение:", _min(line))
print("Максимальное значение:", _max(line))
print("Общая сумма:", _sum(line))
print("Произведение всех чисел:", _mult(line))
print("Остаток при делении суммы на 3:", _delimost(line))
print(f"Затрачено {abs(datetime.now() - start_time)} ")
