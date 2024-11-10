# Algorithm: 
# 1. Define a function should_buy_coupon that takes n, x, y, and prices as input
# 2. Initialize the save variable to 0
# 3. Iterate through the prices
# 4. If the price is greater than or equal to y, add y to the save variable
# 5. Otherwise, add the price to the save variable
# 6. Return "COUPON" if the save variable is greater than x, else return "NO COUPON"

def should_buy_coupon(n, x, y, prices):
    save = 0    # Initialize the save variable to 0
    for price in prices:    
    # Iterate through the prices and check if the price is greater than or equal to y and update the save variable if the condition is not met then add the price to the save variable
        if price >= y:
            save += y
        else:
            save += price
    return "COUPON" if save > x else "NO COUPON"    # Return "COUPON" if the save variable is greater than x else return "NO COUPON"

while True:     # Loop until a valid input is entered
    try:  
    # Try to get the number of test cases and break the loop if the input is valid else print an error message and continue the loop 
        t = 5
        if t <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

while t > 0:
    try:
    # Try to get the values of n, x, y, and prices and call the should_buy_coupon function with the values as arguments and print the result then decrement t by 1 else print an error message  
        n, x, y = map(int, input("Enter n, x, and y (space-separated): ").split())   
        prices = list(map(int, input("Enter prices (space-separated): ").split()))  
        
        print(should_buy_coupon(n, x, y, prices))
        t -= 1
    except ValueError:
        print("Invalid input. Please ensure correct format.")

