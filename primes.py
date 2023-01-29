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

def get_primes(n):
    numbers = set(range(2, n+1, 1))
   
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
      
        numbers.difference_update(set(range(p*2, n+1, p)))
    
    return primes


def getNumber():
    x = 0
    while True:
        try:
            x = input("Enter your number: ")
            x = int(x)
            printLine()
            print("Prime till {} are:".format(x), end=" ")
            print(get_primes(x))

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
        # playFunction()
        getNumber()
        
        x = input("Do you want to play again.(Y/N):")
        if x.lower().startswith("y"):
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
