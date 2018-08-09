# wageCalculator.py
def convertWageMtoW(mWage):
    wageGap = 0.182
    ratio = 1-wageGap
    return ratio*mWage


def approximatelyEqual(expected, val, epsilon):
    ''' Returns true if expected and val are equal within a difference of
        epsilon '''
    diff = abs(expected-val)
    return diff < epsilon

def main():
    epsilon = 0.001
    print("Testing convertMtoW(100)...")
    ans = convertWageMtoW(100)
    expected = 81.8
    # Make sure 
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

    print("Testing convertMtoW(76.2)...")
    ans = convertWageMtoW(76.2)
    expected = 62.3316
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

    print("Testing convertMtoW(0)...")
    ans = convertWageMtoW(0)
    expected = 0.0
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

if __name__ == "__main__": main()
