def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    
try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(F"Discount applied The final price is: { final_price:.2f}")
        else:
            print(f"No discount applied. The final price is: {final_price:.2f}")
except ValueError
            print("please enter valid numbers for price and discount percentage.")
        
