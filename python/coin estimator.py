#coin estimator by weight

def coin_estimator():
    pen = int(input("What is the total weight (in grams) of the pennies?: "))
    nic = int(input("What is the total weight (in grams) of the nickels?: "))
    dim = int(input("What is the total weight (in grams) of the dimes?: "))
    qua = int(input("What is the total weight (in grams) of the quarters?: "))


    pen_co = pen/126
    nic_co = nic/199
    dim_co = dim/113
    qua_co = qua/226

    pen_wrap = pen_co/50
    nic_wrap = nic_co/40
    dim_wrap = dim_co/50
    qua_wrap = qua_co/40

    print("You have " + str("%.2f" % pen_co) + " Pennies, for a total value of $" + str("%.2f" % (pen_co/100)) + ". You will need " + str("%.2f" % pen_wrap) + " coin wrappers to package them all.")
    print("You have " + str("%.2f" % nic_co) + " Nickels, for a total value of $" + str("%.2f" % (nic_co/20)) + ". You will need " + str("%.2f" % nic_wrap) + " coin wrappers to package them all.")
    print("You have " + str("%.2f" % dim_co) + " Dimes, for a total value of $" + str("%.2f" % (dim_co/10)) + ". You will need " + str("%.2f" % dim_wrap) + " coin wrappers to package them all.")
    print("You have " + str("%.2f" % qua_co) + " Quarters, for a total value of $" + str("%.2f" % (qua_co/4)) + ". You will need " + str("%.2f" % qua_wrap) + " coin wrappers to package them all.")

def coin_interface():
    print(coin_estimator())

while True:
    coin_interface()
    cont = input("Do you want to start over? ")
    if cont == "n":
        break




    
    
