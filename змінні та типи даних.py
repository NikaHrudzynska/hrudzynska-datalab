#1
first_name = "Veronika"
last_name = "Hrudzynska"
age = 32

result = f"Мене звати {first_name} {last_name}, мені {age} роки"
print(result)

#2
a = 15
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
integer_division = a //b
remainder = a % b
exponentiation = a ** b

print("addition: ",addition) 
print("subtraction: ",subtraction) 
print("multiplication: ",multiplication)
print("division: ", division)
print("integer_division: ", integer_division)
print("remainder: ", remainder)
print("exponentiation: ", exponentiation)

#3
x = 100
y = 200

x, y = y, x
print("x = ",x)
print("y = ",y)

#4
pi = 3.14159
r = float(input("Введіть радіус кола: "))
s = pi * (r ** 2)
print(s)

#5
usd_to_uah = 37.5
dollar = float(input("Введіть долари: "))
output = round(dollar * usd_to_uah, 2)
print("uah", output)

#6
text = "   PyThOn PrOgRaMmInG   "
text = text.strip()
text = text.lower()
text = text.upper()
text = text.replace("PROGRAMING", "DEVELOPMENT")
text = len(text)
print(text)

#7
first_name = "Тарас"
last_name = "Шевченко"
initials = f"{first_name[0]}." + f"{last_name[0]}."
print(initials)

#8
total_seconds = 3665
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours}:{minutes}:{seconds}")

#9
total_students = 28
present = 23
absent = total_students - present
present_percentage = ((present / total_students) *100)
absent_persentage = round((absent / total_students) * 100, 1)
print("присутні", present_percentage, "%")
print("відсутні", absent_persentage, "%")

#10 Парне чи непарне
int(input("Введіть число: ")) % 2 == 0

#11
price = 1500
discount_percent = 15
sum_of_discount = (price * discount_percent) / 100
final_price = price - sum_of_discount
print("Знижка: ", sum_of_discount)
print("Остаточна ціна: ", final_price)

#12
number = 1234567.891234
print(round(number, 2))
print(f"{number:,}")
print(f"{number:,.2f}")

#13
cost = 250
length = 2.45
name = "Lilith"
on_sale = True
storage = None

print("cost:", cost, type(cost))
print("length:", length, type(length))
print("name:", name, type(name))
print("on_sale:", on_sale, type(on_sale))
print("storage:", storage, type(storage))

#14
weight = float(input("provide your weight in kg: "))
height = float(input("provide your height in m: "))
bmi = weight / (height ** 2)
print(round(bmi,1))

#15
email = " USER@EXAMPLE.COM "
email.strip
email.lower
name , domain = email.split("@")

print("name: ", name)
print("domain: ", domain)

#16
c = float(input("type tempreture in C': "))
f = (c * (9 / 5)) + 32
k = c + 273.15
print("F: ", f)
print("K: ", k)

#17
text = "Python" 
print(text[::-1])

#18
text = "Programming"
print(text[:3])
print(text[-3:])
print(text[::2])

#19
a = 10
b = 20
c = 30
average = (a +b +c) / 3
print(average)

#20
number = 456
hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10
sum = hundreds + tens + ones
print(sum)

#21
product = "Ноутбук"
price = 15000
quantity = 2
together = price * quantity
print(f"Товар: {product}") 
print(f"Ціна: {price} грн") 
print(f"Кількість: {quantity} шт")
print(f"Разом: {together} грн")

#22
password = input("Введіть пароль: ")
print("Довжина не меньше 8 символів: ", len(password) >= 8)
print("Містить цифри: ", any(i.isdigit() for i in password))

#23
speed = 60
distance = 450
time = distance / speed
hours = int(time)
minutes = int((time - hours) * 60)
print(hours,":",minutes)

#24
cost_per_minute = 2.5
minutes = 7
seconds = 30
total_minutes = minutes + seconds/60
total_cost = total_minutes * cost_per_minute
print(total_cost)

#25
number_1 = int(input("Type number 1: "))
number_2 = int(input("Type number 2: "))
print(number_1 % number_2 == 0)

#26
surname = input("Type your surname: ")
name = input("Type your name: ")
patronymic = input("Type your patronymic: ")
print(f"{surname} {name[0]}.{patronymic[0]}")

#27
number = 850
percent = 15
percent_amount = (percent * number) / 100
number_plus_percent = number + percent_amount
number_minus_percent = number - percent_amount

#28
numbers = "123456789"
number_sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3]) + int(numbers[4]) + int(numbers[5]) + int(numbers[6]) + int(numbers[7]) + int(numbers[8])
print(number_sum)

#29
first_name = "Іван"
last_name = "Петров"
birth_year = 2000

username = first_name.lower() + last_name.lower() + str(birth_year)
print(username)

#30
number_1 = float(input("Перше число: ")) !=0
number_2 = float(input("Друге число: ")) !=0
operation = input("Операція (+, -, *, /): ")
operations = {"+": number_1 + number_2,
              "-": number_1 - number_2,
              "*": number_1 * number_2,
              "/": number_1 / number_2}
print(operations[operation])

#31
text = "Hello World Programming"