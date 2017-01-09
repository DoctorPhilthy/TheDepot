from math import sqrt 

def check_pytriple(sides):

    if sqrt(max(sides) ** 2 - min(sides) ** 2) in sides:
        return "This is a triple"
   
    else:
        return "This is not a triple"

def pytriple_interface():
    sides = [int(input("Enter side A length: "))]
    sides += [int(input("Enter side B length: "))]
    sides += [int(input("Enter side C length: "))]
    print(check_pytriple(sides))

while True:
    pytriple_interface()
    cont = input("Do you want to continue?")
    if cont == "n":
        break
