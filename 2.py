from random import randint as rnd


# генерируем файл
def gen(letter, N):
    with open(f'27{letter}.txt', 'w') as f:
        f.write(f'{N}\n')
        for _ in range(N):
            f.write(f"{rnd(1, 25)} {rnd(1, 25)} {rnd(1, 25)}\n")
        f.close()

# подготовка, просто заранее открываем файл и создаем список интов
select = 'test'  # буква файла
gen(select, 4)  # буква + кол-во строк
f = list(map(lambda x: list(map(int, x.split())), open(f'27{select}.txt')))
N = f.pop(0)[0]


# неэфф прога
mx = float('-inf')  # отпадет при 1м сравнении
for row1 in range(N - 2):  # просто перебираем для каждой грядки,
    for k1 in range(3):  # для каждого корнеплода, который хотим удалить,
        for row2 in range(row1 + 1, N - 1):  # все возможные следующие удаления
            for k2 in range(3):
                for row3 in range(row2 + 1, N):
                    for k3 in range(3):
                        all_sum = sum(f[row1])+sum(f[row2])+sum(f[row3])  # сумма ваще всех корнеплодов
                        korneplodi = f[row1][k1] + f[row2][k2] + f[row3][k3]  # сумма удаленных
                        curr_diff = all_sum - korneplodi  # сумма оставшихся
                        if curr_diff % 3 == 0:  # тут проверка усл и поиск макс знач
                            mx = max(mx, korneplodi)
print(mx)


# эфф прога
amogus = {(0, 0): [[], 0]} # key=(сум ост масс % 3, кол-во корнеплодищ); value=[список кп, сум ост масс]
mx = float('-inf')  # для максимума
for i in range(N):
    triple = f[i]  # текущ грядка
    s = sum(triple)  # сум всех кп
    new = {}  # пустой список, туда кинем все возможные соединения
    for old in sorted(amogus, key=lambda x: sum(amogus[x][0])):  # итерация по ключам сортиров. по сумме корнеп. словаря
        data_prev = amogus[old]  # сам элемент
        for k in sorted(triple):  # тоже сортируем чтобы потом перезаписать на бОльшие значения; k = кп
            el = [data_prev[0] + [k], s - k + data_prev[1]]  # итоговое значение после приб. k 
            if len(el[0]) == 3:  # если у нас 3 корнеплода, то сравниваем по усл
                if el[1] % 3 == 0: mx = max(mx, sum(el[0]))
            elif ((el[1] % 3, len(el[0])) not in new) or (sum(el[0]) > sum(new[(el[1] % 3, len(el[0]))][0])):
                # тут крч если этот ключ повтоярется то мы суем его при усл что взяли пожирнее кп
                # но если впервые, то можно не парица
                new[(el[1] % 3, len(el[0]))] = el.copy()  # .copy() на всякий случай
    for el in new:  # копируем типа
        if (el not in amogus) or (sum(new[el][0]) > sum(amogus[el][0])):
            # если опять же ключ повтор и кп взяты пожирнее прежних, то пишем, или если он новый
            amogus[el] = new[el]
print(mx)
