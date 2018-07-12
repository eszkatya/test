# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: array may be empty, in this case return 0.
# Cover your code with tests before writing the actual function
# Think of 'edge cases'
# Ref: https://www.youtube.com/watch?v=_sLByVQm3N4

def positive_sum(arr):
    negativ = []
    pozitiv = []
    for i in arr:
        if i < 0:
            negativ.append(i)
        else:
            pozitiv.append(i)
    return (sum(pozitiv))

print(positive_sum((-1,2,7)))

# Mi volt a feladat, és mit csinál a te algoritmusod?