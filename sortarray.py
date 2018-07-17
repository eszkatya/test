def two_sort(array):
    list = sorted(array)
    #return list
    elso = list[0]
    #return elso
    elso2 = '***'.join(tuple(elso))
    return elso2

print((two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])))

# !:
# def two_sort(lst):
#    return '***'.join(min(lst))
