# wageCalculator.py
def convertWageMtoW(mWage, wageGap):
    ratio = 1-wageGap
    return ratio*mWage


def countryPick(country):
    if   country == "A":
        return .1817
    elif country == "B":
           return .1649
    elif country == "C":
        return .1664
    elif country == "D":
        return .0155
    elif country == "E":
        return .3462
    elif country == "F":
        return .0987
    else:
        print("Please Pick A Country")
        return 0


def main():
    # Presents Menu Options
    print("Please select a country\n"   + \
          "A. USA\n"                    + \
          "B. Meixco\n"                 + \
          "C. UK\n"                     + \
          "D. Romania\n"                + \
          "E. Korea\n"                  + \
          "F. France")

    # Sets rate according to country
    countryRate = countryPick(input("Country (A-F): "))
    
    # Checks for invalid country
    if countryRate == 0:
        quit
    
    maleWage = input("Please enter male wage: ")
    
    femWage = convertWageMtoW(maleWage, countryRate)
    print("The female wage in that country is " + femWage)

if __name__ == "__main__": main()
