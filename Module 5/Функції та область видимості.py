#1
def greet(name):
    print(f"Hello, {name}!")
greet("Ivan")
greet("Maria")
greet("Oleksandr")

#2
def square(n):
    return n**2
for i in range(1, 6):
    print(square(i))

#3
def is_even(n):
    return n % 2 == 0
for i in range(1, 11):
    print(i, is_even(i))

#4
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(5, 3))
print(max_of_two(10, 15))
print(max_of_two(7, 7))

#5
def rectangle_area(width, height):
    return width * height
print(rectangle_area(5, 10))
print(rectangle_area(7, 3))
print(rectangle_area(12, 12))

#6
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(212))

#7
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(17))
print(is_prime(20))
print(is_prime(29))

#8
def count_vowels(text):
    count = 0

    for i in text.lower():
        if i in "aeiou":
            count += 1

    return count

print(count_vowels("Hello World"))
print(count_vowels("Python Programming"))

#9
def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

print(factorial(5))
print(factorial(7))
print(factorial(10))

#10
def reverse_string(text):
    reverse_text = ""

    for i in text:
        reverse_text = i + reverse_text

    return reverse_text

print(reverse_string("Python"))
print(reverse_string("Hello World"))

#11
def power(base, exponent=2):
    return base ** exponent
print(power(5))
print(power(5, 3))
print(power(2, 10))

#12
def greet(name, greeting="Привіт", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Ivan")
greet("Maria", "Hello")
greet("Petro", "Hello", ".")

#13
def create_profile(name, age, city, occupation):
    return f"{name}, {age} years, {city}, {occupation}"

print(create_profile(name="Ivan", age=25, city="Kyiv", occupation="Programmer"))
print(create_profile(city="Lviv", name="Maria", occupation="Designer", age=23))

#14
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))
print(sum_all(5))

#15
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_info(name="Ivan", age=25, city="Kyiv")

#16
def calculate(operation, *numbers, **options):
    if operation == "sum":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        
        for i in numbers:
            result *= i
        
        return result
    
    elif operation == "max":
        return max(numbers)
    
    elif operation == "min":
        return min(numbers)

    if options.get("round", False):
        result = round(result)

    return result
    
print(calculate("sum", 1, 2, 3, 4, 5.3))
print(calculate("multiply", 2, 3, 4))
print(calculate("max", 10, 25, 7, 30, 15))

#17
def divide(a, b):
    return a / b

numbers = [10, 2]
print(divide(*numbers))

params = {"a": 10, "b": 2}
print(divide(**params))

#18
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 7, 1, 9, 2])

print("minimum:", minimum)
print("maximum:", maximum)

#19
def list_stats(numbers):
    return{
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
result = list_stats([1, 2, 3, 4, 5])
print(result)

#20
def split_even_odd(numbers):
    even = []
    odd = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

even_numbers, odd_numbers = split_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("even:", even_numbers)
print("odd:", odd_numbers)

#21
def validate_age(age):
    if 0 <= age <= 120:
        return True, age
    else:
        return False, "Invalid age"

print(validate_age(25))
print(validate_age(150))
print(validate_age(-5))

#22
x = "global"

def test():
    x = "local"
    print("Inside:", x)

test() # виведеться х=local, бо значення х було присвоєно в середині функції

print("Outside:", x) # виведеться х=global, бо значення х було присвоєно перед функцією на глобальному рівні.

#23
counter = 0

def increment():
    global counter
    counter +=1

increment()
increment()
increment()
increment()
increment()
print(counter)

#24
def increment(counter):
    return counter +1

counter = 0

for i in range(5):
    counter = increment(counter)
print(counter)

#25
def outer():
    x = "outer"

    def inner():
        print(x)

    inner()
outer() # виведе outer, бо коли виконуєтся функція outer() вона викликає inner(), а inner() знаходить змінну х у зовнішній функції, якій присвоєно значення outer.

#26
def outer():
    count = 0
    
    def inner():
        nonlocal count # якщо прибрати nonlocal, то виведе error, бо count як локальна змінна ще не має присвоєного значення.
        count += 1
        return count
    
    print(inner())
    print(inner())
    print(inner())

outer() # виведе 1 2 3

#27
square = lambda x: x ** 2
add = lambda a, b: a + b
is_positive = lambda x: x > 0

print(square(5))
print(add(10, 20))
print(is_positive(7))
print(is_positive(-3))

#28
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
doubles = list(map(lambda x: x * 2, numbers))
cubes = list(map(lambda x: x ** 3, numbers))

print(squares)
print(doubles)
print(cubes)

#29
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
greater_than_5 = list(filter(lambda x: x > 5, numbers))
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print(even_numbers)
print(greater_than_5)
print(divisible_by_3)

#30
words = ["apple", "pie", "zoo", "a", "be"]

print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))
print(sorted(words, key=lambda x: x[-1]))

#31
def apply_operation(numbers, operation):
    result = []
    
    for i in numbers:
        result.append(operation(i))
    return result

numbers = [-2, -1, 0, 1, 2]

print(apply_operation(numbers, lambda x: x ** 2))
print(apply_operation(numbers, lambda x: x * 2))
print(apply_operation(numbers, lambda x: abs(x)))

#32
def multiplier(factor):

    def multiply(number):
        return number * factor
    return multiply

times_two = multiplier(2)
times_five = multiplier(5)

print(times_two(10))
print(times_five(10))

#33
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
print(factorial_recursive(5))
print(factorial_recursive(7))

#34
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))

#35
def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(123))
print(sum_digits(9875))

#36
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))
print(power(3, 4))

#37
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
print(gcd(100, 35))

#38
def is_valid_email(email):
    if "@" not in email:
        return False
    
    if len(email) < 5:
        return False
    
    if " " in email:
        return False
    
    at_index = email.index("@")
    
    if "." not in email[at_index:]:
        return False
        
    return True

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid"))
print(is_valid_email("test @mail.com"))