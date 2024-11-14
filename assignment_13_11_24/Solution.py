# Reading value of N : Number of elements in the Array 
N = int (input ("Enter Number of elements in the array : "))

# Reading value of K : Maximum allowed sum or constant value 
K = int (input ("Enter Maximum allowed SUM / Value of K : "))

# Reading the array A and entering elements through a for loop
A = []
print("Enter the elements of the array:")
for _ in range(N):
    element = int(input())  
    A.append(element) 

# To check if only 1 element is present or not 
# If only one element is present we can remove it from the array as it is 

if N == 1:
    print("YES")

else :
    # Initializing a flag to check if a valid pair is found or not 
    flag = False

    # For loop to check for a pair(i,j) where the sum of A[i]+A[j] <= K 
    for i in range(N) :
        for j in range(i+1,N) :
            if A[i]+A[j] <= K :
                flag = True # Change flag when a valid pair is found
                break # Exit the loop when a valid pair is found
        if flag :
            break

    if flag :
        print("YES")# If a valid pair is found print "YES"
    else : 
        print("NO") # If a valid pair is not found print "NO" 



