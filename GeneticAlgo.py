import numpy as np

foundAlready = []
foundAnything = False

#
# Console Input System:
#

numberOfDailyTransactions = int(input())
register = []

for _ in range(numberOfDailyTransactions):
    S = input().split(" ")

    transactionType = S[0]
    transactionAmount = int(S[1])

    register.append((transactionType, transactionAmount))

#
# Input File Reading System

# register = []

# # with open("input1.txt", "r") as f:
# with open("input2.txt", "r") as f:
#     strs = f.readlines()

#     for i in range(1, len(strs)):
#         S = (strs[i].strip()).split(" ")

#         transactionType = S[0]
#         transactionAmount = int(S[1])

#         register.append((transactionType, transactionAmount))
#


def getFitness(chromosome):
    accumulator = 0

    if set(chromosome) == {'0'}:
        return

    for i in range(len(chromosome)):
        if chromosome[i] == "1":
            if register[i][0] == "d":
                accumulator += register[i][1]
            else:
                accumulator -= register[i][1]

    return accumulator


def crossover(chromoX, chromoY):
    crossoverPoint = np.random.randint(1, len(chromoX))

    childChromo = chromoX[:crossoverPoint] + chromoY[crossoverPoint:]

    return childChromo


def mutate(childChromo):
    separatedChromo = [str(char) for char in childChromo]
    mutationPoint = np.random.randint(0, len(childChromo))

    # print(separatedChromo)

    if separatedChromo[mutationPoint] == 0:
        separatedChromo[mutationPoint] = 1
    else:
        separatedChromo[mutationPoint] = 0

    outStr = ""

    for char in separatedChromo:
        # print(char)

        outStr += str(char)

    return outStr


def generateRandomChromosome():
    chromosome = ""

    for _ in range(len(register)):
        chromosome += str(np.random.randint(0, 2))

    return chromosome


def GeneticAlgorithm(mainPopulation):
    currentPopulation = mainPopulation
    currentChromosome = "1" * len(currentPopulation)
    global foundAlready
    global foundAnything

    iterCount = 0

    # print(currentChromosome)

    while True:
        if iterCount < 2**len(currentPopulation):
            if getFitness(currentChromosome) == 0:
                print(currentChromosome)
                break

            childChromo = crossover(
                currentChromosome, generateRandomChromosome())

            childChromo = mutate(childChromo)

            if childChromo not in foundAlready:

                if getFitness(childChromo) == 0:
                    foundAnything = True
                    # print("Output:", childChromo)
                    print(childChromo)
                    break

                # print(childChromo)

                foundAlready.append(childChromo)

        else:
            if not foundAnything:
                print("-1")
            break

        iterCount += 1


def main():
    GeneticAlgorithm(register)


main()
