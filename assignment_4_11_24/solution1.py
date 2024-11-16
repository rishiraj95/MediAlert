# Function to decide whether Chef should buy the coupon
def should_buy_coupon(n, x, y, prices):
    # Total cost without using the coupon
    total_without_coupon = sum(prices)
    
    # Total cost with the coupon applied
    total_with_coupon = sum(max(0, price - y) for price in prices) + x
    
    # Return decision based on which option is cheaper
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Input the number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
results = []
for _ in range(t):
    # Input values for number of items (n), coupon cost (x), and per-item discount (y)
    n, x, y = map(int, input("Enter N, X, Y: ").split())
    
    # Input the list of item prices
    prices = list(map(int, input("Enter the prices: ").split()))
    
    # Store the result of whether to buy the coupon or not
    results.append(should_buy_coupon(n, x, y, prices))

# Output results for all test cases
for result in results:
    print(result)
