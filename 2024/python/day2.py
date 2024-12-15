from enum import Enum
import enum
import re
import string

leftList = list[str]()
rightList = list()
filesEnabled = [
    'day2-1-sample.txt', 
    'day2-1.txt'
]
for file in filesEnabled:
    with open(file) as f:
        for line in f:
            inputs = re.split('\s+', line)
            
            if not len(inputs[1]):
                continue
            leftList.append(inputs)

    print(f"file {file}")

    class Outcomes(Enum):
        UNKNOWN = 0
        DECREASING = 1
        INCREASING = 2
        KNOWN_INVALID = 3
    safes = 0

    def diffInNorms(num, next):
        return abs(num - next) <= 3 and abs(num - next) >= 1
    # third, bruteforce approach:
    # if line is valid (all increasing or all decreasing and within norms) on its own without modifications, continue
    # if not, try removing the current element if current element invalidates constraint on either side

    def lineIsValid(line: str):
        allIncreasing = True
        allDecreasing = True
        prevNum = None
        for idx, str in enumerate(line):
            if idx > 2 and not allDecreasing and not allIncreasing:
                continue
            if not len(str):
                continue
            num = int(str)
            if not prevNum:
                prevNum = num
                continue
            withinNorms = diffInNorms(prevNum, num)
            allIncreasing = allIncreasing and withinNorms and prevNum < num
            allDecreasing = allDecreasing and withinNorms and prevNum > num
            prevNum = num
        return allDecreasing or allIncreasing


    for line in leftList:
        if lineIsValid(line):
            safes += 1
            continue
        sourceLine = line
        try:
            for i in range(len(sourceLine)):
                testLine = sourceLine[0:i] + sourceLine[i + 1:len(sourceLine)+1]
                if(lineIsValid(testLine)):
                    safes += 1
                    raise Exception('done')
        except Exception:
            continue

    print(f"safes {safes}")
exit(0)
### <second approach>

    # for line in leftList:
    #     outcome = Outcomes.UNKNOWN
    #     # safe = True
    #     # allIncreasing = False
    #     # allDecreasing = False
    #     # differenceInNorms = True
    #     # prevNumber = None
    #     print(line)
    #     dampenerTriggered = False
    #     dampenerSkip = False
    #     for idx, number in enumerate(line):
    #         print(f"last outcome - line item {line[idx -1]} - outcome {outcome.name} - dampened {dampenerTriggered}")
    #         if outcome == Outcomes.KNOWN_INVALID:
    #             continue
    #         if dampenerTriggered and not dampenerSkip:
    #             dampenerSkip = True
    #             continue
    #         if not len(number):
    #             continue
    #         num = int(number)

            # look at the current number and next number and try to determine outcome
            # if the outcome is unknown, difference is within norms and it seems decreasing,
            # set the outcome to decreasing
            # else if outcome unknown, difference within norms, seems increasing,
            # set the outcome to increasing

            # if outcome is unknown, difference is not in norms, attempt to skip one over
            # and repeat the above logic, using up the ticket for dampener in the process

            # if outcome is known, take the outcome and try to determine if the next
            # number keeps the constraints (difference in norms, inc/dec)

            # if the next number does not keep constraints, try to skip one over
            # and see whether the constraint is kept then, using up the ticket in the process

            # if the next number is not available, return 


            # try:
            #     next = int(line[idx + 1])
            # except:
            #     continue

            # differenceInNorms = diffInNorms(num, next)

            # if outcome == Outcomes.UNKNOWN and differenceInNorms and next < num:
            #     outcome = Outcomes.DECREASING
            # elif outcome == Outcomes.UNKNOWN and differenceInNorms and next > num:
            #     outcome = Outcomes.INCREASING
            # elif outcome == Outcomes.UNKNOWN and not differenceInNorms and not dampenerTriggered:
            #     try:
            #         skippedOne = int(line[idx + 2])
            #     except IndexError:
            #         # maybe need to handle end-of-list with unknown
            #         continue
            #     dampenerTriggered = True
            #     differenceInNorms = diffInNorms(num, skippedOne)
            #     if differenceInNorms:
            #         if skippedOne > num:
            #             outcome = Outcomes.INCREASING
            #         elif skippedOne < num:
            #             outcome = Outcomes.DECREASING
            #         else:
            #             # try to remove first element and see if that works
                    
            #             differenceInNorms = diffInNorms(next, skippedOne)
            #             if skippedOne < next and differenceInNorms:
            #                 outcome = Outcomes.DECREASING
            #             elif skippedOne > next and differenceInNorms:
            #                 outcome = Outcomes.INCREASING
            #             else:
            #                 outcome = Outcomes.KNOWN_INVALID
            #     else:
            #         # try to remove first element and see if that works
            #         differenceInNorms = diffInNorms(next, skippedOne)
            #         if skippedOne < next and differenceInNorms:
            #             outcome = Outcomes.DECREASING
            #         elif skippedOne > next and differenceInNorms:
            #             outcome = Outcomes.INCREASING
            #         else:
            #             outcome = Outcomes.KNOWN_INVALID
            # elif outcome == Outcomes.DECREASING:
            #     if next < num and differenceInNorms:
            #         continue
            #     elif not dampenerTriggered:
            #         try:
            #             skippedOne = int(line[idx + 2])
            #         except:
            #             dampenerTriggered = True
            #             continue
            #         dampenerTriggered = True
            #         differenceInNorms = diffInNorms(num, skippedOne)
            #         # case of changing direction:
            #         if idx == 1 and skippedOne > num:
            #             outcome = Outcomes.INCREASING
            #             continue
            #         outcome = Outcomes.DECREASING if skippedOne < num and differenceInNorms else Outcomes.KNOWN_INVALID
            #     else:
            #         outcome = Outcomes.KNOWN_INVALID
            # elif outcome == Outcomes.INCREASING:
            #     if next > num and differenceInNorms:
            #         continue
            #     elif not dampenerTriggered:
            #         try:
            #             skippedOne = int(line[idx + 2])
            #         except:
            #             dampenerTriggered = True
            #             continue
            #         dampenerTriggered = True
            #         differenceInNorms = diffInNorms(num, skippedOne)
            #         if idx == 1 and skippedOne < num:
            #             outcome = Outcomes.DECREASING
            #             continue
            #         outcome = Outcomes.INCREASING if skippedOne > num and differenceInNorms else Outcomes.KNOWN_INVALID
            #     else:
            #         outcome = Outcomes.KNOWN_INVALID
### </second approach>
            ### <first approach>

            # if not prevNumber:
            #     allIncreasing = True
            #     allDecreasing = True
            #     prevNumber = num
            #     continue

                
            # if differenceInNorms and allIncreasing:
            #     allIncreasing = num > prevNumber
            # if differenceInNorms and allDecreasing:
            #     allDecreasing = num < prevNumber

            # if differenceInNorms:
            #     differenceInNorms = abs(num - prevNumber) <= 3 and abs(num - prevNumber) >= 1
            # else:
            #     allIncreasing = allDecreasing = False



            # if not dampenerTriggered and ((not allDecreasing and not allIncreasing) or not differenceInNorms):
            #     dampenerTriggered = True

            # if not differenceInNorms and dampenerTriggered:
            #     allDecreasing = False
            #     allIncreasing = False
            # if differenceInNorms and (not dampenerTriggered or allIncreasing):
            #     allIncreasing = num > prevNumber
            # if differenceInNorms and (not dampenerTriggered or allDecreasing):
            #     allDecreasing = num < prevNumber
            # if differenceInNorms:
            #     differenceInNorms = abs(num - prevNumber) <= 3 and abs(num - prevNumber) >= 1
            # print(f"difference in norms {differenceInNorms}, num {num}, prev {prevNumber}")
            # print(f"dampener {dampenerTriggered} inc {allIncreasing} dec {allDecreasing}")
            # prevNumber = num
            
            
    #         # print(f"status: inc - {allIncreasing}")
    #     print(f"outcome - {outcome.name}, dampener used {dampenerTriggered}")
    #     safes += 1 if (outcome == Outcomes.INCREASING or outcome == Outcomes.DECREASING) else 0
    #     ### </first approach 
    # print(f"safe {safes}")

