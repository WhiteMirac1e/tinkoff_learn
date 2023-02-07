text = input("Введите количество сотрудников и время когда уйдет один сотрудник: ")
n = int(text.split()[0])
if n >= 2:
    t = int(text.split()[1])
    if t <= 100:
        lst = input("Введите этажи по возрастанию через пробел: ")
        lst = lst.split()
        nfirst = int(input("Введите номер сотрудника "))
        lst[nfirst-1] = int(lst[nfirst-1])
        if t >= lst[nfirst-1]:
            l1 = int(lst[-1])
            l0 = int(lst[0])        
            result = l1 - l0 
            print(result)
        else:
            l1 = int(lst[nfirst-1])
            l0 = int(lst[-1])
            result = (l1 - 1) + (l0 - 1)
            print(result)
    else:
        print("Вы ввели неподходящее значение. Введите значения больше меньше 100")
else:
    print("Вы ввели неподходящее значение. Введите значения больше 2")
