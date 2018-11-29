# Complete the minimumDistances function below.
def minimumDistances(a):
    # minValue = None
    # for index in range(0, len(a)):
    #     # print('index =', a[index])
    #     for nextIndex in range(index + 1, len(a)):
    #         # print('nextIndex =', a[nextIndex])
    #         if(a[index] == a[nextIndex]):
    #             if(minValue == None or (minValue > (abs(index - nextIndex)))):
    #                 minValue = abs(index - nextIndex)

    # if(minValue == None):
    #     minValue = -1
    # print(minValue)
    # return minValue

    minDict = {}
    minValue = len(a)

    for index in range(len(a)):
        try:
            minValue = min(index - minDict[a[index]], minValue)
        except:
            minDict[a[index]] = index

    if(minValue == len(a)):
        return -1

    return minValue
