### Write your program here
# Function to determine whether Chef should buy the coupon
def should_buy_coupon(n, x, y, prices):
    # Calculate the total cost without any coupon
    total_without_coupon = sum(prices)
    
    # Calculate the total cost with the coupon
    total_with_coupon = sum(max(0, price - y) for price in prices) + x
    
    # Determine if buying the coupon is beneficial
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Read the number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
results = []
for _ in range(t):
    # Read N, X, Y
    n, x, y = map(int, input("Enter N, X, Y: ").split())
    
    # Read the prices of the items
    prices = list(map(int, input("Enter the prices: ").split()))
    
    # Determine whether to buy the coupon or not and store the result
    results.append(should_buy_coupon(n, x, y, prices))

# Print the results for all test cases
for result in results:
    print(result)

