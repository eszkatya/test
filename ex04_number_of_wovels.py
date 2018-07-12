# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
# and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# 'Number of vowels: 5'
# Cover your code with tests before writing the actual function
# Think of 'edge cases':
# What happens, when an empty string is given? What happens, when there is no vowel in the string? Make it user friendly and inform the user!

def numvowels(x):
    vowels = "aeuioAEUIO"
    if x == "":
        return "empty"
    counter = 0
    for i in x:
        if i in vowels:
            counter += 1
    return counter

print(numvowels ('aUto'))


# Az jó, hogy az üres stringeket kezeled az elején (Az 'empty'-nél mondjuk érdemes lenne egyértelmúbbnek lenne,
# a saját dolgod könnyíted meg, ha az ilenekböl szokást csinálsz), de erre nincsenek assertek. Ha mást nem,
# printeket írj a funkcióhívásokra  hogy ha a részfeladatokat oldod meg sorba, akkor lásd, hogy a korábbi megoldottakat
# nem rontja el, vagy írja felül valami.

