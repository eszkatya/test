"""This time we learn two methods to split or merge string:split() and concat(). also learn a good friend of the split() method: join(). It is an Array method. Their usage:

stringObject.split(separator,howmany)
stringObject.concat(string1,string2,...,stringx)
arrayObject.join(separator)"""



def split_and_merge(string, sp):
    separator = sp
    return separator.join(string)

print(split_and_merge("My name is John"," "))
print(split_and_merge("My name is John","-"))
print(split_and_merge("Hello World!","."))
print(split_and_merge("Hello World!",","))

#oké, szóval minden teszten lefut, ha ide átmásolom, de codewarson nem...
