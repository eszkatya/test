def find_needle(haystack):
    helyezes = []
    if "needle" in haystack:
       helyezes = haystack.index("needle")
       return "found the needle at position " + str(helyezes)

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))

"""igazából ez tetszik, mert hasonlít az enyémre:
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))
    
a százalékjek ilyen használatát meg jó lenne végre megértenem
def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')
