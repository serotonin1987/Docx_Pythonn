# def InsertionSort(A):
#     # Проходим по всем элементам списка, начиная с индекса 1
#     for i in range(1, len(A)):
#         key = A[i]  # текущий элемент, который нужно вставить
#         j = i - 1   # индекс предыдущего элемента
        
#         # Сдвигаем элементы списка, которые больше текущего (key), вправо
#         while j >= 0 and A[j] > key:
#             A[j + 1] = A[j]  # сдвигаем элемент на одну позицию вправо
#             j -= 1  # переходим к предыдущему элементу
        
#         # Вставляем текущий элемент в правильное место
#         A[j + 1] = key
    
#     return A

# Пример использования:
# A = [5, 2, 9, 1, 5, 6]
# sorted_A = InsertionSort(A)
# print(sorted_A)

# def SelectionSort(S):
#     for i in range(len(S)- 1 ):
#         kluch = S[i]
#         j = i + 1 
#         while j <= 0 and S[j]< kluch:
#             S[j - 1] = S[j]
#             j += 1 
#         S[j + 1 ] = kluch
#     return
# S = [5, 2, 9, 1, 5, 6]
# sorted_S = SelectionSort(S)
# print(sorted_S)

# def SelectionSort(S):
#     for i in range(len(S) - 1):
#         # Находим минимальный элемент в оставшейся части массива
#         min_index = i
#         for j in range(i + 1, len(S)):
#             if S[j] < S[min_index]:
#                 min_index = j
        
#         # Меняем местами минимальный элемент с текущим
#         S[i], S[min_index] = S[min_index], S[i]
    
#     return S

# S = [5, 2, 9, 1, 5, 6]
# sorted_S = SelectionSort(S)
# print(sorted_S)


# A = [5,2,9,1,5,6]
# print(sorted(A))

# a = [1,2,3,4,5]
# print(len(a))#len считает количество символов

#_____________________________________________________________________________________________________________________________________________________DATETIME

# import datetime

# date = input("Дату в виде ГГГГ-ММ-ДД: ")

# try:
#     date_obj = datetime.datetime.strptime(date,"%Y-%m-%d")

#     week = date_obj.isocalendar()[1]

#     monday = date_obj - datetime.timedelta(days=date_obj.weekday())


#     print(f"Первый понедельник этой недели: {monday}")


# except ValueError:
#     print("Ошибка: введите дату в правильном виде ГГГГ-ММ-ДД.")



# import datetime

# year_input = input("Введите год : ")

# try:
#     year = int(year_input)

#     date = datetime.date(year, 1, 1)

#     while date.weekday() != 6:  
#         date += datetime.timedelta(days=1)

#     sundays = []

#     while date.year == year:
#         sundays.append(date)
#         date += datetime.timedelta(days=7)

#     print(f"\nВсе воскресенья в {year} году:")
#     for sunday in sundays:
#         print(sunday)

# except ValueError:
#     print("Ошибка: введите корректный год.")



# import datetime

# def addYears(d, years):
#     new_year = d.year + years
#     try:
#         return d.replace(year=new_year)
#     except ValueError:

#         if d.month == 2 and d.day == 29:
#             return datetime.date(new_year, 3, 1)
#         else:
#             raise

# print(addYears(datetime.date(2015, 1, 1), -1))  # 2014-01-01
# print(addYears(datetime.date(2015, 1, 1), 0))   # 2015-01-01
# print(addYears(datetime.date(2015, 1, 1), 2))   # 2017-01-01
# print(addYears(datetime.date(2000, 2, 29), 1))  # ✅ 2001-03-01

# import datetime
# import pytz

# def get_utc_and_local_time():

#     utc_now = datetime.datetime.now(pytz.utc)
    
#     local_time = datetime.datetime.now()

#     print("Текущее время по Гринвичу (UTC):", utc_now.strftime("%Y-%m-%d %H:%M:%S"))
#     print("Местное время:", local_time.strftime("%Y-%m-%d %H:%M:%S"))

# get_utc_and_local_time()

# import datetime

# def calculate_days_between_dates(date1, date2):
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
#     date2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
    
#     delta = date2 - date1
    
#     return abs(delta.days)

# date1 = input("Введите первую дату в формате ГГГГ-ММ-ДД: ")
# date2 = input("Введите вторую дату в формате ГГГГ-ММ-ДД: ")

# days_between = calculate_days_between_dates(date1, date2)
# print(f"Количество дней между {date1} и {date2} = {days_between} дней.")

# import datetime

# date1 = input("Введите первую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
# date2 = input("Введите вторую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")

# d1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
# d2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
# delta = d2 - d1

# days, rem = divmod(delta.seconds, 3600)
# hours, rem = divmod(rem, 60)
# minutes, seconds = divmod(rem, 60)

# print(f"{delta.days} дней, {days} часов, {hours} минут, {seconds} секунд.")

# import calendar

# def generate_html_calendar(year, month):
#     cal = calendar.monthcalendar(year, month)
#     html = f"<html><head><title>Календарь {calendar.month_name[month]} {year}</title></head><body><h2>{calendar.month_name[month]} {year}</h2><table border='1'><tr>{''.join([f'<th>{d}</th>' for d in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']])}</tr>"
#     for week in cal:
#         html += "<tr>" + "".join([f"<td>{day if day else '&nbsp;'}</td>" for day in week]) + "</tr>"
#     return html + "</table></body></html>"

# year, month = int(input("Год: ")), int(input("Месяц: "))
# html_calendar = generate_html_calendar(year, month)

# with open("calendar.html", "w", encoding="utf-8") as f:
#     f.write(html_calendar)

# print("Календарь сохранён в 'calendar.html'")

# b = [str(i) for i in range(1, 10)]
# w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# def show(): print("-------------"); [print(f"| {b[i]} | {b[i+1]} | {b[i+2]} |\n-------------") for i in range(0,9,3)]

# def win(p): return any(b[a]==b[b_]==b[c]==p for a,b_,c in w)

# p = 'X'
# print("********** Игра Крестики-нолики для двух игроков **********")
# while True:
#     show()
#     m = input(f"Куда поставим {p}? ")
#     if m.isdigit() and b[int(m)-1] not in ['X','O']:
#         b[int(m)-1] = p
#         if win(p): show(); print(f"Игрок {p} победил!"); break
#         if all(i in ['X','O'] for i in b): show(); print("Ничья!"); break
#         p = 'O' if p == 'X' else 'X'
#     else:
#         print("Некорректный ход.")

# import math

# fact = lambda n: 1 if n==0 else n*fact(n-1)
# fib = lambda n: n if n<=1 else fib(n-1)+fib(n-2)
# trig = {
#     'sin': lambda x: math.sin(math.radians(x)),
#     'cos': lambda x: math.cos(math.radians(x)),
#     'tan': lambda x: math.tan(math.radians(x)),
#     'asin': lambda x: math.degrees(math.asin(x)),
#     'acos': lambda x: math.degrees(math.acos(x)),
#     'atan': lambda x: math.degrees(math.atan(x)),
# }

# print("Инженерный калькулятор. Введите 'exit' для выхода.")
# while True:
#     op = input("\nОперация (+ - * / % // ** factorial fibonacci sin cos tan asin acos atan): ")
#     if op == 'exit': break
#     try:
#         if op in ['+', '-', '*', '/', '%', '//', '**']:
#             a, b = float(input("a = ")), float(input("b = "))
#             print("Результат:", eval(f"{a}{op}{b}"))
#         elif op == 'factorial':
#             n = int(input("n = "))
#             print(f"{n}! =", fact(n))
#         elif op == 'fibonacci':
#             n = int(input("n = "))
#             print(f"F({n}) =", fib(n))
#         elif op in trig:
#             x = float(input("x = "))
#             print(f"{op}({x}) =", trig[op](x))
#         else:
#             print("Неизвестная операция.")
#     except Exception as e:
#         print("Ошибка:", e)

# from docx import Document
# d = Document(); d.add_paragraph('Hello Python'); d.save('hello.docx')

# from docx import Document
# print(' '.join(run.text for p in Document('hello.docx').paragraphs for run in p.runs if run.bold))

# from docx import Document
# from docx.shared import Pt
# from docx.oxml.ns import qn
# d = Document(); r = d.add_paragraph().add_run('Пример форматированного текста')
# r.font.name = 'Arial'; r.font.size = Pt(16)
# r._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
# d.save('styled.docx')


class Auto:
    def __init__(self):
        self.__model = ""
        self.__year = 0
        self.__manufacturer = ""
        self.__engine_volume = 0.0
        self.__color = ""
        self.__price = 0.0

    # Метод для ввода данных
    def input_data(self):
        self.__model = input("Введите модель автомобиля: ")
        self.__year = int(input("Введите год выпуска: "))
        self.__manufacturer = input("Введите производителя: ")
        self.__engine_volume = float(input("Введите объем двигателя (в литрах): "))
        self.__color = input("Введите цвет машины: ")
        self.__price = float(input("Введите цену: "))

    # Метод для вывода данных
    def display_data(self):
        print(f"Модель: {self.__model}")
        print(f"Год выпуска: {self.__year}")
        print(f"Производитель: {self.__manufacturer}")
        print(f"Объем двигателя: {self.__engine_volume} л")
        print(f"Цвет: {self.__color}")
        print(f"Цена: {self.__price}тг.")

    # Методы доступа (геттеры)
    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_volume(self):
        return self.__engine_volume

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    # Методы установки (сеттеры)
    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_engine_volume(self, volume):
        self.__engine_volume = volume

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price
