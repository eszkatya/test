#Get the number n (n>0) to return the reversed sequence from n to 1.

#Example : n=5 >> [5,4,3,2,1]
def reverse_seq(n):
    a = []
    for i in range(1, n + 1):
        a.append(i)
    #print(a)
    a.reverse()
    #print(a)
    return a

print(reverse_seq(10))


