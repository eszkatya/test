#Define a function that removes duplicates from an array of numbers and returns it as a result.

#The order of the sequence has to stay the same.

def distinct(seq):
    return set(seq)



print (distinct([1]))
print(distinct([1, 2]))
print(distinct([1, 1, 2]))
print(distinct([1, 1, 1, 2, 3, 4, 5]))
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))

#oké, szóval minden teszten lefut, ha ide átmásolom, de codewarson nem...