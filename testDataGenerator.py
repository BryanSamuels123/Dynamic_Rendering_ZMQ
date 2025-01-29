import random
import json

# This program makes some arbitrary dBm values for testing
# Author: Bryan Samuels
# Date 28 Jan 2025


# ranges
# 0-30 bad
# 30-45: less bad
# 45-60: fair
# 60-90: good
dummy_data = []
dataset = []

#  function to add the dBm values to the list
def push(boundaryVal, curr):
    dummy_data.append(boundaryVal + (.2 * curr))


# create dummy values for the bins
# trying to simulate dBm values
counter = 0
for i in range(0, 91, 6):
    if i < 30:
        push(-100, counter)
        if counter == 29:
            counter = 0
    elif i < 45:
        push(-80, counter)
        if counter == 14:
            counter = 0
    elif i < 60:
        push(-60, counter)
        if counter == 14:
            counter = 0
    else:
        push(-45, counter)
    
    counter += 1
    

# append a the reversed list and remove extra value
dummy_data.extend(list(reversed(dummy_data)))
dummy_data.pop()


doneSet = set()
dataset.append(dummy_data.copy())


# create the rest of data
for _ in range(3000):

    # choose 17 psuedorandom values to change
    for _ in range(17):
        randNum = random.randint(0, 30)

        # until a number that hasn't been chosen yet is chosen continue randomly choosing
        while randNum in doneSet:
            randNum = random.randint(0, 30)
        doneSet.add(randNum)


    for i in doneSet:
        noiseVal = random.uniform(0.9, 1.1)
        dummy_data[i] = dataset[0][i] * round(noiseVal, 2)

    dataset.append(dummy_data.copy())
    doneSet.clear()

print()

for i in dataset:
    print(i, end="\n\n")


with open("testData.json", "w") as fh:
    json.dump(dataset, fh)






