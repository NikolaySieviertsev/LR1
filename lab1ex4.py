"""
Task 4
You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not (hence you cannot take a fraction
of a bar).
Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.
The first parameter contains 'capacity' - integer describing the capacity of a knapsack.
The next parameter contains 'weights' - list of weights of each gold bar.
Output : Maximum weight of gold that fits into a knapsack with capacity of W.
"""

bagpackCapacity = int(input("Enter the knapsack capacity: "))
numOfBars = int(input("Enter the number of golden bars: "))


def knapsack(bagpackCapacity, numOfBars):
    maxWeight = 0
    listOfBarsWeight = []
    listMaxWeight = []
    print("Enter the weight of each golder bar: ")
    for i in range(1, numOfBars + 1):
        barWeight = int(input())
        listOfBarsWeight.append(barWeight)

    listOfBarsWeight.sort()
    listOfBarsWeight.reverse()

    for n in range(len(listOfBarsWeight)):
        for j in range(n, len(listOfBarsWeight)):
            maxWeight += listOfBarsWeight[j]
            if maxWeight > bagpackCapacity:
                maxWeight = maxWeight - listOfBarsWeight[j]
        listMaxWeight.append(maxWeight)
        maxWeight = 0

    print("Max weight of gold that fits into a knapsack with capacity of ", bagpackCapacity, " is ", max(listMaxWeight))
    # print(listOfBarsWeight)
    # print(listMaxWeight)
    # print(max(listMaxWeight))

    return bagpackCapacity, numOfBars


knapsack(bagpackCapacity, numOfBars)
