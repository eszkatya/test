def split_and_merge(string, sp):
    separator = sp
    return separator.join(string)

print(split_and_merge("My name is John"," "))
print(split_and_merge("My name is John","-"))
print(split_and_merge("Hello World!","."))
print(split_and_merge("Hello World!",","))

#oké, szóval minden teszten lefut, ha ide átmásolom, de codewarson nem...