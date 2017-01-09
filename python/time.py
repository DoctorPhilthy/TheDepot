import time

x = input("Can I rest a little? yes or no: ")

while True:
    if x == "yes":
        time.sleep(5)
        print("Ah... thanks. I feel refreshed.")

    else:
        print("Is there no rest for the weary?")

    cont = input("Continue? y/n: ")
    if cont == "n":
        break
