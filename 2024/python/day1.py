import re


leftList = list()
rightList = list()
for file in ['day1-1-sample.txt', 'day1-1.txt']:
    print(file)
    with open(file) as f:
        for line in f:
            inputs = re.split('\s+', line, 1)
            
            if not len(inputs[1]):
                continue
            leftList.append(int(inputs[0]))
            rightList.append(int(inputs[1]))

    leftList.sort()
    rightList.sort()

    partOne = 0
    partTwo = 0

    for i in range(len(leftList)):
        left = leftList[i]
        right = rightList[i]
        partOne += abs(left - right)

        if left in rightList:
            firstIndexRight = rightList.index(left)
            lastIndexRight = len(rightList) - 1 - rightList[::-1].index(left)
            partTwo += left * (lastIndexRight - firstIndexRight + 1)



    print(f"Day 1 p1 answer: {partOne}")

    print(f"Similarity score calculation: {partTwo}")

