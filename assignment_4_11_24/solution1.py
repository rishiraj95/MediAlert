### Write your program here
# N - Number of items in the shop
# X - Discount coupon price
# Y - The amount by which the price of every item is reduced
# C - The array containing the price of every item Ai

""" Example
N X Y
4 30 10
C = 15 8 22 6
"""
C = [15,8,22,6]
X = 40
Y = 10

cost_without_coupon = sum(C)

cost_with_coupon = X

for c in C:
    new_price = c-Y
    if new_price<=0:
        new_price=0
    cost_with_coupon+=new_price

if cost_with_coupon<=cost_without_coupon:
    print("COUPON")
else:
    print("NO COUPON")
