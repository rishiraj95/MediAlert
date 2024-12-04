### Write your program heredef solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        # Read the values of N, X, Y
        N, X, Y = map(int, input().split())
        
        # Read the prices of the items
        A = list(map(int, input().split()))
        
        # Calculate the total cost without coupon
        total_no_coupon = sum(A)
        
        # Calculate the total cost with coupon
        total_with_coupon = X  # The cost of the coupon itself
        for price in A:
            if price <= Y:
                total_with_coupon += 0  # Item becomes free
            else:
                total_with_coupon += (price - Y)  # Item is discounted
        
        # Compare the costs and decide
        if total_with_coupon < total_no_coupon:
            print("COUPON")
        else:
            print("NO COUPON")

# Read input and call the function
solve()
