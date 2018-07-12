# Create a function that prints a triangle like this, use [userinput]:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

userinput = int(input("pick a number!"))

def haromszog(userinput):
    for i in range(1,(userinput+1)):
        print (i * "$") 
        # print ("\n")
        
    
haromszog(3)

#  a képen nem pont így néz ki, nem tudtad megoldani vagy így akartad?

