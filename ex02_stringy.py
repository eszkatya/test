# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
# the string should start with a 1.
# a string with size 6 should return :'101010'.
# with size 4 should return : '1010'.
# with size 12 should return : '101010101010'.
# The size will always be positive and will only use whole numbers.

def stringy(size):
    hossz = len(size)
    ures = []
    while hossz != 0:
        for i in range(0,len(size)):
            if i % 2 == 0:
                ures.append(str(1))
            else:
                ures.append(str(0))
        hossz = hossz - 1
        return ''.join(ures)

print (stringy ('kati'))


# NameError: name 'ures' is not defined
# Miert agyaztal be 1 loopot egy másikba? Milyen hosszan kell ismételnünk a feladatot?
#
# if __name__ == "__main__":
#     assert stringy('balint') == '101010', 'balint went wrong'
#     assert stringy('kati') == '1010', 'kati went wrong'
#     assert stringy(' adam') == '1010', 'did you think about whitespaces?'
