"""



"""
# imported libraries
import os

#global variables
# main welcome intro text
mainIntroText = """Welcome to 0001 Prime Factorization
        (1,2,3,5,7......)
    """
########################################################################
# return factors of n


def factors(n): return [x for x in range(2, n+1) if not n % x]

# check if n is prime


def primeChecker(n): return len(factors(n)) == 1

# return prime factors of n


def primeFactorization(n):
    if n < 2:
        return n
    if primeChecker(n):
        return str(n)
    else:
        pf = [x for x in filter(primeChecker, factors(n))]
    return str(pf[0]) + "*" + primeFactorization(int(n/pf[0]))

# get input Number and run primeFactorization


def getNumber():
    x = 0
    while True:
        try:
            x = input("Enter your number: ")
            x = int(x)
            printLine()
            print("Prime factorization of {}:".format(x), end=" ")
            print(primeFactorization(x))

        except:
            print("Enter valid Number")
            continue
        break


########################################################################
# Print new line.
# Can have argument to print multiple Lines
def printLine(n=1):
    print("-"*22 + "\n"*n)

# ClearConsole


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


# this is main function where all calls happens for the script
# User will be asked again and again to play until exits
def main():

    while True:
        # Call Main Function()
        getNumber()

        x = input("Do you want to play again.(Y/N):")
        if x.lower() == "y":
            clearConsole()
            continue
        else:
            break

    print("\n\n---------------------\n Thank You :)\nCome Back Soon\n CodedBy:0001\n---------------------")
    printLine(2)
    x = input("Press any key to exit:")


# Start the script if its opened directly
if __name__ == '__main__':
    print(mainIntroText)

    main()


"""



"""