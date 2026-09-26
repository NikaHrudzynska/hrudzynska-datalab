#1
age = int(input("Введіть вік: "))
if age < 12:
    print("Дитина")
if age >12 and age <17:
    print("Підліток")
if age >= 18:
    print("Дорослий")

#2
digit = int(input("Введіть число: "))
if digit % 2 == 0:
    print("Парне")
else:
    print("Непарне")

#3
digit_1 = int(input("Введіть число 1: "))
digit_2 = int(input("Введіть число 2: "))
if digit_1 == digit_2:
    print("Числа рівні")
elif digit_1 > digit_2:
    print(digit_1)
elif digit_2 > digit_1:
    print(digit_2)

#4
purchase_sum = float(input("Введіть суму покупки: "))
discount_0 = 1
discount_5 = (purchase_sum * 5) / 100
discount_10 = (purchase_sum * 10) / 100
final_amount_5 = purchase_sum - discount_5
final_amount_10 = purchase_sum - discount_10

if purchase_sum < 1000:
    print("Знижка 0%", "Фінальна сума: ", purchase_sum)
if purchase_sum > 1000 and purchase_sum < 5000:
    print("Знижка 5%: ", discount_5, "Фінальна сума: ", final_amount_5)
if purchase_sum > 5000:
    print("Знижка 10%: ", discount_10, "Фінальна сума: ", final_amount_10)

#5
score = int(input("Введіть кількість балів: "))
if score >= 90:
    print("Відмінно")
if score >= 75:
    print("Добре")
if score >= 60:
    print("Задовільно")
if score < 60:
    print("Незадовільно")

#6
a = float(input("Provide a number 1: "))
b = float(input("Provide a number 2: "))
op = input("provide an operation (+, -, *, /): ")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/" and b != 0:
    print(a/b)
elif op == "/" and b == 0:
    print("Error")

#7
year = int(input("Provide a year: "))
if year % 400 == 0:
    print("Високосний")
if year % 4 == 0:
    print("Високосний")
if year % 100 == 0:
    print("Не Високосний")
else:
    print("Не високосний")

#8
a = float(input("Введіть першу сторону: "))
b = float(input("Введіть другу сторону: "))
c = float(input("Введіть третю сторону: "))
if a + b > c and a + c > b and b + c > a:
    print("Трикутник може існувати")
else:
    print("Трикутник не може існувати")

#9
month = int(input("Введіть номер місяця: "))
if month == 12 or month == 1 or month == 2:
    print("Зима")
if month == 3 or month == 4 or month == 5:
    print("Весна")
if month == 6 or month == 7 or month == 8:
    print("Літо")
if month == 9 or month == 10 or month == 11:
    print("Осінь")

#10
a = float(input("Fisrt number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)

#11
a = 0
while a < 11:
    print(a)
    a += 1

#12
n = int(input("What's your number: "))
sum = 0
for i in range(1, n+1):
    sum += i 
print(sum)

#13
for i in range(2,21,2):
    print(i)

#14
n = int(input("Type your number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial: ", factorial)

#15
n = int(input("Type your N: "))
for i in range(n, 0, -1):
    print(i)

#16
number = 21
for i in range(7):
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Congrats!")
        break
    elif guess < number:
        print("Greater")
    else:
        print("Smaller")

#17
total = 0
count = 0
while total <= 100:
    number = int(input("Type your number: "))
    total += number
    count += 1
print("Numbers amount: ", count)
print("Sum of numbers: ", total)

#18
number = 2
while number < 1000:
    print(number)
    number *= 2

#19
number = int(input("Type number: "))
while number < 1 or number >10:
    number = int(input("Type number: "))
print("Thanks!")

#20
n = int(input("Type number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

#20
for i in range(1, 21):
    print(i)

#21
a = int(input("Введіть A: "))
b = int(input("Введіть B: "))
sum = 0
for i in range(a, b + 1):
    sum += i
print("Сума:", sum)

#22
number = int(input("Type number: "))
for i in range(1, number + 1):
    if i % 3 == 0:
        print(i)

#23
text = "Python"
for i in range(len(text)):
    print(i, text[i])