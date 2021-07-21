def rotate(ar,d,n):
    #list_1 = ar[0:d+1]
    #list_2 = ar[d:]
    list_final = ar[d:]+ar[:d]
    print (list_final)

#ar = []
print ("Enter size:")
n = int(input())
print ("Enter point of slicing:")
d = int(input())
print("Enter the array:")
ar = list(map(int, input().split(" ")))
#print(ar)
rotate(ar,d,n)