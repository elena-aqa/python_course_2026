# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a, b):
    return a + b

result = sum_numbers(5, 7)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

result = calculate_average([10, 20, 30, 40, 50])
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

result = reverse_string("Hello")
print(result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(words):
    return max(words, key=len)


result = find_longest_word(["cat", "elephant", "dog", "mouse"])
print(result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
def has_more_than_ten_unique_chars(text):
    """Returns True if the text contains more than 10 unique characters, otherwise returns False."""
    unique_chars = set(text)
    return len(unique_chars) > 10


input_text = "Hello, world!"
print(has_more_than_ten_unique_chars(input_text))

# task 8
def get_only_strings(items):
    """Returns a list containing only string values from the provided list."""
    string_items = []

    for item in items:
        if isinstance(item, str):
            string_items.append(item)

    return string_items


mixed_items = [1, "hello", 3.14, "QA", True]
print(get_only_strings(mixed_items))

# task 9
def sum_even_numbers(numbers):
    """Returns the sum of all even numbers in the provided list."""
    even_numbers_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_numbers_sum += number

    return even_numbers_sum


numbers_list = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(numbers_list))

# task 10
def contains_letter_h(word):
    """Returns True if the word contains letter 'h' or 'H', otherwise returns False."""
    return "h" in word.lower()


input_word = "Hello"
print(contains_letter_h(input_word))
