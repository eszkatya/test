def abbrevName(name):
    splitelt = name.split(" ")
    first = splitelt[0]
    print (first)
    last = splitelt[1]
    print (last)
    monogram = first[0] + '.' + last[0]
    return monogram

print((abbrevName("Sam Harris")))