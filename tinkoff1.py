# Костя подключен к мобильному оператору «Мобайл». Абонентская плата Кости составляет
# ﻿AA﻿ рублей в месяц. За эту стоимость Костя получает ﻿BB﻿ мегабайт интернет-трафика. 
# Если Костя выйдет за лимит трафика, то каждый следующий мегабайт будет стоить ему 
# ﻿CC﻿ рублей.
# Костя планирует потратить ﻿DD﻿ мегабайт интернет-трафика в следующий месяц. 
# Помогите ему сосчитать, во сколько рублей ему обойдется интернет.
import time 
start = time.time()

abonpay = int(input("Введите стоимость абоненской платы: "))
if 1<= abonpay <=100:
    mb = int(input("Введите количество мб трафика: "))
    if 1<= mb <=100:
        cost = int(input("Введите переплату за каждый мегабайт: "))
        if 1<= cost <=100:
            traffic = int(input("Введите запланированные расходы трафика в мб: "))
            if 1<= traffic <=100:
                if mb <= traffic:
                    result = abonpay + (traffic - mb) * cost
                    print(f"Расходы кости на интернет: {result}")
                else:
                    result = abonpay
                    print(f"Расходы кости на интернет: {result}")
            else:
                print("Вы ввели неподходящее значение. Введите значения в интервале от 1 до 100") 
        else:
            print("Вы ввели неподходящее значение. Введите значения в интервале от 1 до 100") 
    else:
        print("Вы ввели неподходящее значение. Введите значения в интервале от 1 до 100") 
else:
        print("Вы ввели неподходящее значение. Введите значения в интервале от 1 до 100")

end = time.time() - start ## собственно время работы программы

print(end)
