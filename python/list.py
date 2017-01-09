import random

list1 = ['physics', 'chemistry', 'biology', 'philosophy']
list2 = ['baseball', 'basketball', 'football', 'soccer']

x = random.randint(0, 3)
y = random.randint(0, 3)

a = random.randint(0, 1)

print("Sports vs. Sciences\n")

if a == 1:
    print(str(list2[x]) + " is better than " + str(list1[y]))

else:
    print(str(list1[x]) + " is better than " + str(list2[y]))