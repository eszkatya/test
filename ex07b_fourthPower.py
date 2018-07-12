# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
from .ex07a_square import square
# You should use the square procedure that you defined in an earlier exercise by importing the file's specific function
#  and reusing it in your function via calling it

def fourthPower(y, x):

    z = square(y)
    while x > 2:
        z = z * y
        x -= 1
    return z
      
print(fourthPower(2, 3))


#  A feladatban az importálásnak kellett volna utána nézni egy másik fileból.
# A funkciók egymásba ágyazásával mit értél el, mi történik lépésenként a függvény hívásakor?
