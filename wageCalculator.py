# wageCalculator.py
def main():
    """ Presents Menu Options """
    print("Please select a country\n"   + \
          "A. USA\n"                    + \
          "B. Meixco\n"                 + \
          "C. UK\n"                     + \
          "D. Romania\n"                + \
          "E. Korea\n"                  + \
          "F. France")

    # Sets rate according to country
    countryRate = countryPick(input("Country (A-F): "))
    
    # Prompts for a number entry
    maleWage = recordNumber("\nPlease enter the male wage: $ ") 

    femWage = convertWageMtoW(maleWage, countryRate)
    print("\nThe female wage in that country is $ " + str(femWage))

def countryPick(country):
"""  Returns country wage gap, and rejects invalid country entries """
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
        print("Please pick a country\n")
        exit()

def recordNumber(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("That is not a valid number\n")
        exit()

def convertWageMtoW(mWage, wageGap):
    ratio = 1-wageGap
    return ratio*mWage

if __name__ == "__main__": main()
