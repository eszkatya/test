def find_needle(haystack):
    if "needle" in haystack:
       helyezes = haystack.index("needle")
       #return type(helyezes)
       return "found the needle at position" + " "+str(helyezes)

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))