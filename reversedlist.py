#Get the number n (n>0) to return the reversed sequence from n to 1.

#Example : n=5 >> [5,4,3,2,1]

def reverse_seq(n):
    ures = list(range(1,n+1)) # tudom, hogy nem elegáns, de nem tudom, mit lehetne helyette
    print(ures)
    ures.reverse()
    return ures



print(reverse_seq(6))