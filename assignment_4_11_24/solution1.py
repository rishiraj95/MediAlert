# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N (number of items), X (cost of coupon), Y (discount threshold)
    N, X, Y = map(int, input().split())
    # Read the list of item prices
    A = list(map(int, input().split()))
    
    # total cost price without coupon
    total_cost_without_coupon = sum(A)
    
    # total cost price with coupon
    total_cost_with_coupon = X
    for price in A:
        if price > Y:
            total_cost_with_coupon += price - Y
        # If price <= Y, the item is free (i.e., no extra cost for that item)

    # Compare the two total costs
    if total_cost_with_coupon < total_cost_without_coupon:
        print("COUPON")
    else:
        print("NO COUPON")
or Smarter Healthcare Insights