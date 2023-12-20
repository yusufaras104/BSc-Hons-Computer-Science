"""
Write a python program to simulate an online store. The program should begin by displaying
a list of products and their prices. There should be a minimum of 4 products offered. The
program should ask the user to choose a product and then ask the user to enter the quantity
they require of that product. The program should then allow the user to keep choosing more
products and quantities until they enter something to indicate they want to end the program
(e.g. a given number or 'q' or 'exit'). The program should then tell the user the total
amount for the products they have selected.
"""
!pip install pyfiglet
!pip install inquirer
!pip install tabulate
import pyfiglet
from tabulate import tabulate

# Table of Products
result = pyfiglet.figlet_format("Yusuf", font="5lineoblique")
print("\t**********************************************")
print("\t***        Welcome Task 8 Python Shop      ***")
print(f"{result}")
print("\t**********************************************")
print("𝖂𝖊𝖑𝖈𝖔𝖒𝖊")
product_line = [
    [1, 'Iphone 12', f'£{650}', '⭐⭐⭐⭐'],
    [2, 'Iphone 14', f'£{799}', '⭐⭐⭐'],
    [3, 'Iphone SE', f'£{150}', '⭐⭐⭐⭐⭐'],
    [4, 'Samsung S21', f'£{544}', '⭐⭐']
]

print("Welcome to the online Smart Phone store!\nThese are the smart phones we offer:\n")
print(tabulate(product_line, headers=['#', 'Name', '£ Price', 'Awards'], tablefmt='fancy_grid'))

buy_another_flag = True
total_cost = 0

while buy_another_flag:
    product_choice = input("What would you like to buy (Enter product number or 'q' to quit): ")
    if product_choice == 'q':
        break

    product_index = int(product_choice) - 1

    if 0 <= product_index < len(product_line):
        quantity = int(input("Enter the quantity: "))
        price = float(product_line[product_index][2].strip('£'))
        subtotal = price * quantity
        total_cost += subtotal

        print(f"The price is: £{subtotal:.2f}")
    else:
        print("Invalid product number.")

    buy_another_choice = input("Would you like to buy another item? (y/n): ")
    if buy_another_choice.lower() != 'y':
        buy_another_flag = False

print(f"The total price of your basket is: £{total_cost:.2f}")