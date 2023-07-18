from random import randint as rnd
from statistics import mean  # для удобства, можно и через sum/len делать, но это не так красиво

# генерируем файл
def gen(letter, N):
    with open(f'27{letter}.txt', 'w') as f:
        f.write(f'{N}\n')
        for _ in range(N):
            f.write(f"{rnd(1, 5)}\n")
        f.close()


# подготовка, просто заранее открываем файл и создаем список интов
select = 'test'  # буква файла
gen(select, 19)  # буква + кол-во строк
f = list(map(int, open(f'27{select}.txt')))
N = f.pop(0)

# неэффективная прога
ans = {}
for i in range(1, N - 9):  # 1й по усл мимо, последние 9 не трогаем тоже по усл
    rate = f[i]  # берем оценку дома
    to_take = i  # изначально берем слева все дома, переменная = скок домов слева возьмем
    if rate < (i + 1): to_take = rate  # если оценка <= кол-во домов слева, то оценку юзаем

    left_mean = mean(f[(i - to_take): i])  # взяли ср арифм левых домов
    right_mean = mean(f[(i + 1): (i + 10)])  # и справа

    print(i + 1, '|', left_mean, rate, right_mean)  # просто посмотреть инфу о доме и его соседях
    if left_mean < rate < right_mean:  # подходящий дом
        # print("\033[91m", i + 1, rate, "\033[0m")  # номер + оценка
        if rate not in ans: ans[rate] = float('inf')  # если с такой оценкой никого нет то созд с беск номером
        ans[rate] = min(i + 1, ans[rate])
print()
print(max(ans.items(), key=lambda x: x[0])[1])  # ответ!


# эффективная
# просто собираем преф суммы
pref = [0]
for rate in f:
    pref.append(rate + pref[-1])

ans = {}
for i in range(1, N - 9):  # аналогично неэфф, но теперь мы left и right mean берем через преф. суммы
    rate = f[i]
    to_take = i
    if rate < (i + 1): to_take = rate

    left_mean = (pref[i] - pref[i-to_take])/to_take
    right_mean = (pref[i+10] - pref[i+1])/9

    if left_mean < rate < right_mean:  # подходящий дом
        if rate not in ans: ans[rate] = float('inf')
        ans[rate] = min(i + 1, ans[rate])
print()
print(max(ans.items(), key=lambda x: x[0])[1])
