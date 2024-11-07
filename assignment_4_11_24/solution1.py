# Function to determine if Chef should buy the discount coupon
def should_buy_coupon(n, x, y, prices):
    # Calculate total price without using the discount coupon
    total_without_coupon = sum(prices)
    
    # Calculate total price with the discount coupon
    total_with_coupon = 0
    for price in prices:
        # If the price of an item is less than or equal to Y, it becomes free
        if price <= y:
            total_with_coupon += 0
        else:
            # Apply the discount to the item, ensuring it doesn't go below zero
            total_with_coupon += price - y
    
    # Add the coupon cost to the total price when using the coupon
    total_with_coupon += x
    
    # Decide if buying the coupon is beneficial
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Input handling
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    # Reading values for each test case
    n, x, y = map(int, input().split())
    prices = list(map(int, input().split()))
    
    # Store the result for each test case
    results.append(should_buy_coupon(n, x, y, prices))

# Output results for each test case
for result in results:
    print(result)
