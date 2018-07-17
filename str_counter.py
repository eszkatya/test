# meg kellett adni egy stringet és egy betűt, utóbbi előfordulását megszámoltatni a stringben
#https://www.codewars.com/kata/abbreviate-a-two-word-name/train/python
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
