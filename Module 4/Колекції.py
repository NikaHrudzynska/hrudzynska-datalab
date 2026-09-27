#1
movies = ["Тіні забутих предків", "Пропала грамота", "Miller's crossing", "Earth", "Girl with a needle"]
print(movies[0])
print(movies[-1])
print(movies[2])
print(len(movies))

#2
shopping = []
shopping.append("cheese")
shopping.append("water")
shopping.append("coffee")
shopping.insert(1, "chair")
shopping.extend(["juice", "melon"])
print(shopping)

#3
numbers = [10, 20, 30, 40, 50, 60, 70]
numbers.remove(30)
print(numbers)
numbers.pop()
print(numbers)
del numbers[0]
print(numbers)

#4
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[:3])
print(fruits[-2:])
print(fruits[2:6])
print(fruits[::2])
print(fruits[::-1])

#5
scores = [85, 92, 78, 90, 88, 76, 95, 89]
scores.sort()
print(scores)
desc_scores = sorted(scores, reverse=True)
print(scores)
print(desc_scores)

#6
numbers = [5, 12, 17, 9, 3, 12, 8, 12, 15]
print(numbers.count(12))
print(numbers.index(12))
print(20 in numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#7
original = [1, 2, 3, 4, 5]
reference = original #створює посилання на original, зміни будуть відображатися в обох списках
copy1 = original.copy() #створює незалежну копію списку original за методом copy
copy2 = original[:] #створює незалежну копію списку original за допомогою зрізу
original[0] = 99 #

print(original)
print(reference)
print(copy1)
print(copy2)

#8
squares = [i ** 2 for i in range(1, 11)]
print(squares)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

words = ["cat", "elephant", "dog", "butterfly"]
length = [len(i) for i in words]
upper_words = [i.upper() for i in words]
print(length)
print(upper_words)

#9
list1 = [1, 2, 3]
list2 = [4, 5, 6]

first = list1 + list2
print(first)

second = list1.copy()
second.extend(list2)
print(second)

third = list1 * 2 +list2
print(third)

#10
grades = [45, 78, 89, 34, 67, 92, 56, 88, 72, 95]
passed = [i for i in grades if i >= 60]
excellent = [i for i in grades if i >= 90]
failed = len([i for i in grades if i < 60])
avg = sum(grades) / len(grades)
print(passed)
print(excellent)
print(failed)
print(avg)

#11
coords = (10, 20, 30)
one_coord = (5,)
empty = ()
different = (1, "text", 0.21, True, [3, 5] )
print(type(coords))
print(type(one_coord))
print(type(empty))
print(type(different))

#12
person = ("Іван", 25, "Київ", "ivan@example.com", "+380501234567")
print(person[0])
print(person[1])
print(person[-1])
print(person[:3])
print(person[::-1])

#13
data = ("Python", 3.11, 2023, True)
language, version, year, is_popular = data
print(language)
print(version)
print(year)
print(is_popular)
language, is_popular = is_popular, language

#14
numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2, 7)
print(numbers.count(2))
print(numbers.index(4))
print(len(numbers))
print(max(numbers))
print(min(numbers))

#15
colors = ("red", "green", "blue")
new_colors = ("yellow,") + colors
print(new_colors)

list = list(colors)
list[0] = "yellow"
colors = tuple(list)
print(colors)

