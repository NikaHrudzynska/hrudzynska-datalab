import pandas as pd
import numpy as np

file_path = r"C:\Users\veronika.hrudzynska\OneDrive - Accenture\Desktop\Data_Lab\Python\Pandas\Sample - Superstore Sales (Excel).xls"

#Структура аркушів

# Orders містить основну інформацію про замовлення, зокрема такі стовпці:
# Row ID, Order ID, Order Date, Ship Date, Ship Mode, Order Priority, Customer Name, 
# Customer Segment, Province, Region, Product Category, Product Sub-Category, Product Name, 
# Product Container, Product Base Margin, Unit Price, Shipping Cost, Sales, Order Quantity, 
# Discount, Profit.

# Returns: Order ID, Status.
# Users: Region, Manager.

#1
orders = pd.read_excel(
    file_path,
    sheet_name="Orders",
    engine="xlrd")

returns = pd.read_excel(
    file_path,
    sheet_name="Returns",
    engine="xlrd")

users = pd.read_excel(
    file_path,
    sheet_name="Users",
    engine="xlrd")

print("Версія pandas:", pd.__version__)

#2
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

#3
print("Перші 5 рядків:")
print(orders.head())

print("Останні 5 рядків:")
print(orders.tail())

#4
print("Кількість рядків:", orders.shape[0])
print("Кількість стовпців:", orders.shape[1])

print("Типи даних:")
print(orders.dtypes)

#5
orders.info(memory_usage="deep")
memory_by_column = orders.memory_usage(
    index=False,
    deep=True
).sort_values(ascending=False) #найбільше пам'яті займають текстові стовпці

print(memory_by_column)

#6
numeric_statistics = orders.describe(
    include=[np.number]
)

print(numeric_statistics)

text_statistics = orders.describe(
    include=["object"]
)

print(text_statistics)

#7
print(
    "Product Category:",
    orders["Product Category"].nunique()
)

print(
    "Product Sub-Category:",
    orders["Product Sub-Category"].nunique()
)

print(
    "Region:",
    orders["Region"].nunique()
)

ship_mode_percent = (
    orders["Ship Mode"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(ship_mode_percent)