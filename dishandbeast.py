def feast(beast, dish):
   if beast[0] == dish[0] and beast[-1] == dish[-1]:
       return "True"
   else:
       return "False"

print (feast("great blue heron", "nyamnyam"))



#def feast(beast, dish):
#    return beast.startswith(dish[0]) and beast.endswith(dish[-1])
#startswith és endswith újak.

#def feast(beast, dish):
#    return beast[0] == dish[0] and beast[-1] == dish[-1]    
# fölösleges volt az enyém iffel
