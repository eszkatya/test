#Write function avg which calculates average of numbers in given list.

#Python:
#Due to rounding issues please do not use statistics.mean or such.
#If the array is empty, return 0.


def find_average(array):
    szamlalo = sum(array)
    nevezo = len(array)
    atlag = szamlalo / nevezo
    return atlag

print(find_average(( 1, 2, 9 )))

#ezek jók:
#def find_average(array):
#    return sum(array) / len(array) if array else 0

 #def find_average(array):
 #   return 0 if not array else sum(array) / len(array)

"""ez érdekes, még nem értettem meg:
def find_average(array):
    if not array:
        return 0

    class SafeFloat(object):
        def __init__(self, val):
            super(SafeFloat, self).__init__()
            self.val = val

        def __eq__(self, float_val):
            # let me fix your comparisons..
            def isclose(a, b):
                return abs(a - b) < 0.00000001
            return isclose(self.val, float_val)

        def __str__(self):
            return str(self.val)

    from numpy import mean
    return SafeFloat(mean(array))
