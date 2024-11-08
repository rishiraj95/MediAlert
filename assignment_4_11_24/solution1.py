def should_buy_coupon(N, X, Y, prices):
    # N: Number of items in the shop
    # X: Cost of the discount coupon
    # Y: Discount provided by the coupon on each item
    
    # Calculate the total price without the coupon
    total_without_coupon = sum(prices)
    
    # Initialize the total price with the coupon cost
    total_with_coupon = X
    
    for price in prices:
        # Calculate the discounted price of the item
        # If price - Y is less than or equal to 0, the item becomes free
        discounted_price = max(0, price - Y)
        
        # Add the discounted price to the total price with the coupon
        total_with_coupon += discounted_price
    
    # Determine if Chef should buy the coupon
    # If the total price with the coupon is less than the total price without the coupon
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Read number of test cases
T = int(input("Enter the number of test cases: "))
results = []

for _ in range(T):
    # Read N (number of items), X (cost of coupon), Y (discount amount)
    N, X, Y = map(int, input("Enter N (number of items), X (cost of coupon), Y (discount amount): ").split())
    
    # Read the prices of the N items
    prices = list(map(int, input("Enter the prices of the items separated by spaces: ").split()))
    
    # Determine if Chef should buy the coupon for this test case
    results.append(should_buy_coupon(N, X, Y, prices))

# Print the results for all test cases
for result in results:
    print(result)
