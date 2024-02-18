def calculate_total_cost(unit_price,quantity):
    total_cost = unit_price * quantity
    if total_cost > 1000:
        discount = total_cost * 0.10
        total_cost -= discount
        print("Total cost after 10% discount:",total_cost)
    else:
        print("Total cost:", total_cost)

unit_price = float(input("Enter the unit price of the item:"))
quantity = int(input("Enter the quantity purchased:"))

calculate_total_cost(unit_price,quantity)