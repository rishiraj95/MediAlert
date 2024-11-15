"""
input:

n = 3

i = 1
size of list1 = 2
list1 = [1,2]

i = 2
size of list2 = 4
list2 = [2,2,3,4]

i = 3
size of list3 = 1
list3=[1]

output:

1
2
0

""" 


#initializing n for number of times to iterate through the the loop for input
n=int(input())

#initializing empty list to k

k=[]
for i in range(n):
    #size of list
    a=int(input())

    #list initialization
    l=list(map(int,input().split()))
    #length of list minus count of minimum number in the list
    m=len(l)-l.count(min(l))

    #appending the values to k
    k.append(m)
#iterate through k (result)
for i in k:
    print(i)
