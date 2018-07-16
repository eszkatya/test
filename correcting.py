def correct(string):
    return string.replace("1", "I").replace("5","S").replace("0","O")

print(correct("DUBL1N"))

#def correct(string):
#    return string.translate(str.maketrans("501", "SOI"))
# string.translate és str.maketran utánanézni

#def correct(string):
#    return string.replace('1','I').replace('0','O').replace('5','S')
# string.replacenek utánanázni
