def get_quantity(record):
    return record[2]

def main():
    print("Welcome to Inventory List Analyzer!")
    print()
    
    inventory_records = []
    item_dict = {}
    unique_categories = set()
    quantities = []
    
    running = True
    while running:
        name = input("Enter item name: ")
        name = name.strip()
        
        category = input("Enter category: ")
        category = category.strip()
        category = category.lower()
        
        quantity_str = input("Enter quantity: ")
        quantity = int(quantity_str)
        
        inventory_records.append((name, category, quantity))
        item_dict[name] = quantity
        unique_categories.add(category)
        quantities.append(quantity)
        
        choice = input("Do you want to add more items? (y/n): ")
        choice = choice.strip()
        choice = choice.lower()
        print()
        
        if choice != 'y':
            running = False
            
    if len(inventory_records) == 0:
        print("No items recorded in the inventory.")
        return

    total_different_items = len(inventory_records)
    
    item_names = []
    for record in inventory_records:
        item_names.append(record[0])
        
    names_str = ""
    for i in range(len(item_names)):
        if i == 0:
            names_str = item_names[i]
        elif i == len(item_names) - 1:
            names_str = names_str + ", and " + item_names[i]
        else:
            names_str = names_str + ", " + item_names[i]
            
    total_quantity = 0
    for q in quantities:
        total_quantity = total_quantity + q
        
    avg_quantity = total_quantity / total_different_items
    
    max_qty = quantities[0]
    min_qty = quantities[0]
    most_stocked_name = inventory_records[0][0]
    least_stocked_name = inventory_records[0][0]
    
    for item in inventory_records:
        it_name = item[0]
        it_qty = item[2]
        
        if it_qty > max_qty:
            max_qty = it_qty
            most_stocked_name = it_name
            
        if it_qty < min_qty:
            min_qty = it_qty
            least_stocked_name = it_name
            
    print("============ INVENTORY SUMMARY ============")
    print()
    
    print("Total Different Items:", total_different_items)
    print("Explanation: You entered", total_different_items, "different items:", names_str + ".")
    print()
    
    q_expr = ""
    for i in range(len(quantities)):
        q_expr = q_expr + str(quantities[i])
        if i < len(quantities) - 1:
            q_expr = q_expr + " + "
            
    print("Total Quantity in Stock:", total_quantity)
    print("Explanation: Sum of all quantities:", q_expr, "=", total_quantity)
    print()
    
    print("Average Quantity per Item:", avg_quantity)
    print("Explanation: Average =", total_quantity, "total /", total_different_items, "items")
    print()
    
    print("Most Stocked Item:", most_stocked_name, "(" + str(max_qty) + " units)")
    print("Explanation:", most_stocked_name, "has the highest quantity among all items.")
    print()
    
    print("Least Stocked Item:", least_stocked_name, "(" + str(min_qty) + " units)")
    print("Explanation:", least_stocked_name, "has the lowest quantity.")
    print()
    
    print("-" * 45)
    print()
    print("Unique Categories in Inventory:", unique_categories)
    print("Explanation: Categories are taken from user input and converted to lowercase.")
    print("No duplicates are shown here.")
    print()
    print("-" * 45)
    
    sorted_items = sorted(inventory_records, key=get_quantity, reverse=True)
    print()
    print("📦 Items Sorted by Quantity (High to Low):")
    print()
    
    idx = 1
    for item in sorted_items:
        print(str(idx) + ".", item[0] + " - " + str(item[2]) + " units")
        idx = idx + 1
        
    print()
    print("Explanation: Items are sorted using the quantity field from highest to lowest.")
    print()
    print("-" * 45)
    
    categories_list = list(unique_categories)
    sorted_categories = sorted(categories_list)
    print()
    print("📁 Categories in Alphabetical Order:")
    print()
    
    idx = 1
    for cat in sorted_categories:
        print(str(idx) + ".", cat)
        idx = idx + 1
        
    print()
    print("Explanation: The set of unique categories was sorted alphabetically for display.")
    print()
    print("============ END OF REPORT ============")

if __name__ == "__main__":
    main()