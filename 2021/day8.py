## Import Input Data ##
with open("2021\day8.txt") as fileObject:
    inputLines = fileObject.readlines()

splitLists = []
for line in inputLines:
    [inputList, outputList] = line.split("|")
    splitLists.append([inputList.strip(), outputList.strip()])

    outputSum = 0
    for [inputList, outputList] in splitLists:
        inputs = inputList.split()
        outputs = outputList.split()

        # find outputs corresponding to 1, 4, 7 and 8
        knownOutputs = {2: 1, 4: 4, 3: 7, 7: 8}
        solvedDigits = {}
        for input in inputs:
            try:
                solvedDigits[knownOutputs[len(input)]] = input
            except KeyError:
                pass

        # find outputs corresponding to 2, 5, and 6
        [firstChar, secondChar] = solvedDigits[
            1
        ]  # 2, 5, and 6 will only have one signal contained in 1
        firstCandidates = [
            string
            for string in inputs
            if firstChar in string and secondChar not in string
        ]
        secondCandidates = [
            string
            for string in inputs
            if secondChar in string and firstChar not in string
        ]

        solvedDigits[2] = min([firstCandidates, secondCandidates], key=len)[0]
        solvedDigits[5] = min(
            max([firstCandidates, secondCandidates], key=len), key=len
        )
        solvedDigits[6] = max(
            max([firstCandidates, secondCandidates], key=len), key=len
        )

        # find outputs corresponding to 0, 3, 9
        candidates = [
            string for string in inputs if string not in list(solvedDigits.values())
        ]
        smallestString = min(candidates, key=len)
        solvedDigits[3] = smallestString
        del candidates[candidates.index(smallestString)]  # signal correspinding to 3

        fourChars = solvedDigits[4]  # signals contained in four
        # find the central signal
        for char in fourChars:
            for candidate in candidates:
                if char not in candidate:
                    centralSignal = char

        solvedDigits[9] = [string for string in candidates if centralSignal in string][
            0
        ]
        solvedDigits[0] = [
            string for string in candidates if centralSignal not in string
        ][0]

        # add up all outputs
        outputString = ""
        for output in outputs:
            for outputVal in range(10):
                if sorted(output) == sorted(solvedDigits[outputVal]):
                    outputString += str(outputVal)
                    break

        outputSum += int(outputString)

print(f"The sum of the outputs is: {outputSum}")
