def find_average(array):
    szamlalo = sum(array)
    nevezo = len(array)
    atlag = szamlalo / nevezo
    return atlag

print(find_average(( 1, 2, 9 )))