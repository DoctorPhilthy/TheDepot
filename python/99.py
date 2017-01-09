

words = [' bottles', ' of beer', ' on the wall\n', '\n', 'Take one down\n', 'Pass it around\n']

for i in range(99, 0, -1):
    if i == 1:
        print(str(i) + " bottle" + words[1] + words[2] + str(i) + " bottle" + words[1] + words[3] + words[4] + words[5] + "No" + words[0] + words[1] + words[2])

    else:
        print(str(i) + words[0] + words[1] + words[2] + str(i) + words[0] + words[1] + words[3] + words[4] + words[5] + str(i - 1) + words[0] + words[1] + words[2])
