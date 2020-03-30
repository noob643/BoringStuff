import random

numberOfStreaks = 0 
while True: #I added a while loop to see how the probability would change with different data samples
    #Code that creates 
    data = [] 
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        data_set = []
    # Code that creates a list of 100 'heads' or 'tails' values.
        for z in range(100):
            if random.randint(0, 1) == 0:
                data_set.append("H")
            else:
                data_set.append("T")
        data.append(data_set)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for x in range(len(data)):
        specimen = "".join(str(z) for z in data[x])
        cond1 = "TTTTTT"
        cond2 = "HHHHHH"
        if (cond1 or cond2) in specimen:
            numberOfStreaks += 1

    print("Chance of streak: %s%%" % (numberOfStreaks / 100))
