def str_count(strng, letter):
    counter = 0
    for i in strng:
        if i == letter:
            counter += 1
    return counter

print(str_count('Hello', 'b'))