def apply_discount(price, discount):
    # 1. Check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"
        
    # 2. Check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
        
    # 3. Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
        
    # 4. Check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
        
    # 5. Calculate and return the discounted price
    return price - (price * (discount / 100))

# Test case
print(apply_discount(100, 20))  # Expected Output: 80.0
