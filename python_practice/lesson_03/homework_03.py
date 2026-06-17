# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, '
    '"if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print(alice_in_wonderland.count("'"))

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_area = black_sea + azov_sea

print(f"Площа Чорного та Азовського морів разом: {total_area} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
first_second = 250449
second_third = 222950

warehouse_1 = total_goods - second_third
warehouse_2 = first_second - warehouse_1
warehouse_3 = second_third - warehouse_2

print(f"Кількість товарів на Складі №1: {warehouse_1} шт")
print(f"Кількість товарів на Складі №2: {warehouse_2} шт")
print(f"Кількість товарів на Складі №3: {warehouse_3} шт")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
payment_period = 18
computer_price = monthly_payment * payment_period

print(f"Вартість комп’ютера: {computer_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"Остача від ділення 8019 : 8 = {8019 % 8}")
print(f"Остача від ділення 9907 : 9 = {9907 % 9}")
print(f"Остача від ділення 2789 : 5 = {2789 % 5}")
print(f"Остача від ділення 7248 : 6 = {7248 % 6}")
print(f"Остача від ділення 7128 : 5 = {7128 % 5}")
print(f"Остача від ділення 19224 : 9 = {19224 % 9}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza_quantity = 4
large_pizza_price = 274

medium_pizza_quantity = 2
medium_pizza_price = 218

juice_quantity = 4
juice_price = 35

cake_quantity = 1
cake_price = 350

water_quantity = 3
water_price = 21

large_pizza_total = large_pizza_quantity * large_pizza_price
medium_pizza_total = medium_pizza_quantity * medium_pizza_price
juice_total = juice_quantity * juice_price
cake_total = cake_quantity * cake_price
water_total = water_quantity * water_price

total_order_price = large_pizza_total + medium_pizza_total + juice_total + cake_total + water_total

print(f"Повна вартість замовлення {total_order_price} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
total_pages = total_photos // photos_per_page
print(f"Для альбому потрібно {total_pages} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
consumption = 9
consumption_distance = 100
tank_capacity = 48

total_fuel = distance / consumption_distance * consumption
total_tanks_needed = total_fuel / tank_capacity

# при умові, що родина стартує подорож з повним баком вже
refills_quantity = total_tanks_needed - 1

print(f"Для подорожі знадобиться {int(total_fuel)} літри бензину")
print(f"Під час подорожі потрібно заправитися {int(refills_quantity)} рази")



