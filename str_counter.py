def str_count(strng, letter):
    counter = 0
    for i in strng:
        if i == letter:
            counter += 1
    return counter

print(str_count('Hello', 'b'))

#izginek tűnik, de nem értem:
#str_count=lambda x,y:x.count(y)#(strng, letter):

# ami sokkal szebb:
#def strCount(string, letter):
#    return string.count(letter)
