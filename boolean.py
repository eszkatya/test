#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
    
"""ezt is lehetett vna egy sorba, ami még érdekes:
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
bár nem teljesen értem, hogy ez h működik
 
