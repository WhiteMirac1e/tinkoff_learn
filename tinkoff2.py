N = int(input("Введите количество частей рулета: "))
if 1 <= N <= 2*10**9:
    if N % 2 == 0:
        result = N // 2
        print(result)
    else:
        result = N // 2 + 1
        print(result)
else:
    print("Вы ввели неподходящее значение. Введите значения в интервале от 1 до 2000000000")
