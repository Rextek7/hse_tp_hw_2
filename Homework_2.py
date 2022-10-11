from datetime import datetime
from tqdm import tqdm



f = 'Numbers.txt'
with open(f) as file:
    file_ = file.read().split(' ')
line = [int(item) for item in file_]


start_time = datetime.now()

def _at_all(line):
    return len(line)



def _min(line):
    _mn = 10 ^ 8
    _mn = min(line)
    return _mn



def _max(line):
    _mx = max(line)
    return _mx



def _sum(line):
    _sm = sum(line)
    return _sm



def _mult(line):
    _mult = 1
    for i in tqdm(line):
        _mult = (_mult * i)
    return _mult



def _delimost(line):
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
