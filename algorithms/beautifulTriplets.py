
def beautifulTriplets(d, arr):
    # older solution
    # print('d = ', d)
    # count = 0
    # for value in range(0, len(arr)):
    #     gotFirstValue = None
    #     print('&&&&&&&&&&&&&&&&&&&&&&& arr[value] = ', arr[value])
    #     for restOfValues in range(value + 1, len(arr)):
    #         print('----- arr[restOfValues] =', arr[restOfValues])
    #         print('gotFirstValue = None', gotFirstValue == None)
    #         print('arr[restOfValues] - arr[value] =', arr[restOfValues] - arr[value])
    #         print('value - nextVlaue = d', arr[restOfValues] - arr[value] == d)
    #         if(gotFirstValue == None and (arr[restOfValues] - arr[value] == d)):
    #             print('found first part of the triplet')
    #             gotFirstValue = arr[restOfValues]
    #         if(gotFirstValue != None):
    #             print('gotFirstValue is = ', gotFirstValue)
    #             if(arr[restOfValues] - gotFirstValue == d):
    #                 print('count += 1')
    #                 count += 1
    # print('total count is =', count)
    # return count
    count = 0
    for value in range(len(arr)):
        if arr[value] + d in arr and arr[value] + 2*d in arr:
            count += 1
    return count
