# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
