from datetime import datetime

print("Введите название файла:")
f = Numbers.txt
with open(f) as file:
    file_ = file.read().split(' ')
line = [int(item) for item in file_]

k = _sm = _mx = _del = 0
_mn = 10^8

start_time = datetime.now()

def _at_all(k):
    for i in range(len(line)):
        k += 1
    return k

def _min(_mn):
    for i in range(len(line)):
        _mn = min(_mn, line[i])
    return _mn

def _max(_mx):
    _mx = max(line)
    return _mx

def _sum(_sm):
    _sm = sum(line)
    return _sm

def _mult(line):
    _mult = 1
    for i in (line):
        _mult = (_mult * i)
    return _mult

def _delimost(_del):
    _sum = sum(line)
    _del = _sum % 3
    return _del

print("Количество чисел:", _at_all(k))
print("Минимальное значение:", _min(_mn))
print("Максимальное значение:", _max(_mx))
print("Общая сумма:", _sum(_sm))
print("Произведение всех чисел:", _mult(line))
print("Остаток при делении суммы на 3:", _delimost(_del))
print(f"Затрачено {abs(datetime.now() - start_time)} ")


