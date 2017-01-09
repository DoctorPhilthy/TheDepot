import random



print("I am the Magic 8 Ball... I know all\n")

while True:

    q = input("\nAsk a Yes or No question: ")


    answers = ["Outcome is Hazy", "It is certain", "Yes", "Definitely", "Ask again later", "Cannot predict now", "Signs point to yes", "Fat chance", "Dream on", "No Way", "Doubtful... very doubtful..."]

    a = random.randint(0, 9)
    print("\n ... \n ... \nThinking... \n ... \n")
    print(answers[a])

    cont = input("\nDo you want to continue? y/n: ")
    if cont == "n":
        break


