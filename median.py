my_list = [1,2,3,4,5,6,7]

def median(m):
    n = len(m) 

    if my_list == []:
        return "None"

    if n % 2 == 0:
        median1 = m[n // 2]
        median2 = m[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = m[n // 2]
    return {str(median)}

print(median(my_list))


def testMedian():
    assert(testMedian(1,2,3,4,5,6) == 3.5)
    assert(testMedian(1,3,7,9,10) == 7)
    assert(testMedian(1) == 1)
    assert(testMedian() == "None")
    assert(testMedian(1,10) == 5)