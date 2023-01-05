primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

tokenPositions = {"Token1": 5, "Token2": 6}

diceRolled = [2, 3]
operations = ["+", "-", "*", "/"]

def anylizeAllOptions():
    results = []
    for firstOperation in operations:
        for secondOperation in operations:
            # print(tokenPositions["Token1"], firstOperation, diceRolled[0], secondOperation, diceRolled[1])
            # print(tokenPositions["Token1"], firstOperation, diceRolled[1], secondOperation, diceRolled[0])
            results.append([tokenPositions["Token1"], firstOperation, diceRolled[0], secondOperation, diceRolled[1]])
            results.append([tokenPositions["Token1"], firstOperation, diceRolled[1], secondOperation, diceRolled[0]])
            results.append([tokenPositions["Token2"], firstOperation, diceRolled[0], secondOperation, diceRolled[1]])
            results.append([tokenPositions["Token2"], firstOperation, diceRolled[1], secondOperation, diceRolled[0]])

    # print(results)
    possiblePlays, possibleResults = readResults(results)
    # print(possiblePlays, possibleResults)
    findBestPlay(possiblePlays, possibleResults)

def findBestPlay(possiblePlays, possibleResults):
    maxResult = 0
    for result in possibleResults:
        if result - possiblePlays[possibleResults.index(result)][0] > maxResult:
            maxResult = result - possiblePlays[possibleResults.index(result)][0] 
    print("Your best play is to move you pawn at " + str(possiblePlays[possibleResults.index(result)][0]) + " to " + str(maxResult + possiblePlays[possibleResults.index(result)][0]) + " (" + str(diceRolled[0]) +", "+ str(diceRolled[1]) + ")")


def readResults(results):
    possiblePlays = []
    possibleResults = []
    for result in results:
        firstCalculation = calculate(result[0], result[1], result[2])
        # print(firstCalculation)
        if not (checkResult(firstCalculation)):
            continue
        secondCalculation = calculate(firstCalculation, result[3], result[4])
        # print(secondCalculation)
        if not (checkResult(secondCalculation)):
            continue
        possiblePlays.append(result)
        possibleResults.append(secondCalculation)
    return possiblePlays, possibleResults

def checkResult(x):
    if x > 101:
        return False
    if x // 1 != x:
        return False
    if x < 0:
        return False
    return True

def calculate(int1, operand, int2):
    if operand == "+":
        return int1 + int2

    if operand == "*":
        return int1 * int2

    if operand == "-":
        return int1 - int2

    if operand == "/":
        return int1 / int2

anylizeAllOptions()