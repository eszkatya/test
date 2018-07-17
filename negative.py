 #itt csak negatívvá kellett tenni egy számot..nem volt semmilyen kitétel. Nem tom bemásolni a feladatot
 #mert 3. frissítés után is errort ad a codewars

def make_negative(number):
    number = str(number)
    if number[0] == "-" or (number == "0"):
        return int(number)
    else:
        number2 = int(number) * -1
    return number2

print(make_negative(0))

"""hát itt kábé minden elegánsabb mint az enyém
def make_negative( number ):
    return -abs(number)
ezek szerint a mínusz jelent nem csak egy konkrét szám elé használtom
