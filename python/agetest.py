
a = int(input("What is your birth year?"))
young = ("Too Young!")
old = ("Welcome to adulthood")

if a > 1996:
    print(young)
    c = input("So what do you want to be when you grow up?")
    if c == "Doctor":
	    print("Good. Make your family proud")
    if c != "Doctor":
	    print("Not a Doctor? You are a disappointment")

if a <= 1996:
    print(old)
    b = input("so how does it feel?")
    if b == "Great!":
        print("congratulations… now go pay your damn bills")
    if b != "Great!":
        print("Well, you better get used to it, loser")