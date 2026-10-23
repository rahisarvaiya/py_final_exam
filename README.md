# Inventory List Analyzer – Store Stock Review

## Description
A Python console application that simulates a small store's stock review system. The app collects inventory items, processes them, and provides comprehensive summary insights using basic string handling, loops, control structures, collections, and built-in sorting logic.

## Features
- **Control Structures & Looping:** Collects multiple item inputs using standard `while` loops and conditional statements.
- **String Handling:** Standardizes text data by stripping whitespace and converting item categories to lowercase.
- **Collection Datatypes:** Utilizes dictionaries, lists of tuples, and sets to manage and organize inventory records.
- **Built-in Functions & Calculations:** Calculates totals, averages, and identifies most/least stocked items using standard Python logic.
- **Sorting Logic:** Automatically sorts items by quantity in descending order and unique categories alphabetically.

## Assumptions
- Quantities are entered as valid integers.
- Item categories are automatically normalized to lowercase for uniqueness checks.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Save the code into a file named `inventory_analyzer.py`.
3. Run the script using your terminal or command prompt:
   ```bash
   python inventory_analyzer.py
   ```

## Sample Output
```text
Welcome to Inventory List Analyzer!

Enter item name: Milk
Enter category: Dairy
Enter quantity: 10
Do you want to add more items? (y/n): y

Enter item name: Rice
Enter category: Grain
Enter quantity: 50
Do you want to add more items? (y/n): y

Enter item name: Salt
Enter category: Spice
Enter quantity: 5
Do you want to add more items? (y/n): y

Enter item name: Sugar
Enter category: Grain
Enter quantity: 40
Do you want to add more items? (y/n): n

============ INVENTORY SUMMARY ============

Total Different Items: 4
Explanation: You entered 4 different items: Milk, Rice, Salt, and Sugar.

Total Quantity in Stock: 105
Explanation: Sum of all quantities: 10 + 50 + 5 + 40 = 105

Average Quantity per Item: 26.25
Explanation: Average = 105 total / 4 items

Most Stocked Item: Rice (50 units)
Explanation: Rice has the highest quantity among all items.

Least Stocked Item: Salt (5 units)
Explanation: Salt has the lowest quantity.

---------------------------------------------

Unique Categories in Inventory: {'grain', 'dairy', 'spice'}
Explanation: Categories are taken from user input and converted to lowercase.
No duplicates are shown here.

---------------------------------------------

📦 Items Sorted by Quantity (High to Low):

1. Rice - 50 units
2. Sugar - 40 units
3. Milk - 10 units
4. Salt - 5 units

Explanation: Items are sorted using the quantity field from highest to lowest.

---------------------------------------------

📁 Categories in Alphabetical Order:

1. dairy
2. grain
3. spice

Explanation: The set of unique categories was sorted alphabetically for display.

============ END OF REPORT ============
```

## Author
RAHI SARVAIYA
