#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot seperating them.
#It should look like this:
#Sam Harris => S.H
#Patrick Feeney => P.F

def abbrevName(name):
    splitelt = name.split(" ")
    first = splitelt[0]
    print (first)
    last = splitelt[1]
    print (last)
    monogram = first[0] + '.' + last[0]
    return monogram.upper

print((abbrevName("Sam Harris")))

#def abbrevName(name):
#    first, last = name.upper().split(' ')
#   return first[0] + '.' + last[0]

# first és last definiálását nem értem...hogy hogy vesszővel elválasztjuk?

# ez tetszik:
#def bool_to_word(bool):
#return "Yes" if bool else "No"
