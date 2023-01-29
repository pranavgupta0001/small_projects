
########################################################################

"""
Strings operations
1: reverse(string)
2: fizzBuzz(number)


"""

class String():

    """
    Reverse a String - Enter a string and the program will reverse it and print it out.


    """

    def reverse(string):

        # string is like list in array so using [::-1] to revrse it
        return string[::-1]

        # Method 2
        #y =list(string)
        # y.reverse()
        # return "".join(y)



    """
    Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print “Fizz” instead of the number and 
    for the multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five print “FizzBuzz”.
    """


    def fizzBuzz(n):
        for i in range(1,n+1):
            divideByThree = i%3
            divideByFive = i%5
            if divideByThree==0 and divideByFive==0:
                print("FizzBuzz")
            elif divideByThree==0:
                print("Fizz")
            elif divideByFive==0:
                print("Buzz")
            else:
                print(i)


    """
    Pig Latin is a way of altering English Words. The rules are as follows:

    - If a word begins with a consonant, take the first consonant or 
    consonant cluster, move it to the end of the word, and add "ay" to it.

    - If a word begins with a vowel, just add "way" at the end.

    """

    def pigLatin(string):
        vowels = ["a","o","e","u","i"]
        for index,word in enumerate(string):
            if word in vowels and index==0:
                return(string+"way")
            if word in vowels:
                return string[index:]+string[:index]+"ay"
        return string+"ay"

        
    """
    Count Vowels - Enter a string and the program counts 
    the number of vowels in the text. For added 
    complexity have it report a sum of each vowel found
    """
    def countVowels(string):
        count = {}
        vowels = "aoeui"
        for word in string:
            if word in vowels:
                count[word] = count.get(word,0)+ 1
        return count

    """
    Check if Palindrome - Checks if the string 
    entered by the user is a palindrome. That 
    is that it reads the same forwards as backwards like “racecar”
    """
    def palindrome(string):
        return String.reverse(string) == string

    """
    Count Words in a String - Counts the number of individual 
    words in a string. For added complexity read these strings 
    in from a text file and generate a summary
    """
    def CountWords(string= None,file=None):
        if string:
            return "Words in '{}' are: {}".format(string,len(string))
        if file:
            try:
                with open(file,"r") as f:
                    countLines = 0
                    countWords =0
                    for line in f:
                        countLines+=1
                        countWords+= len(line)
                    return(f"In file {file}:\n\tLines:{countLines}\n\tWords:{countWords}")
            except:
                print("Error: No file found")
                

if __name__ == '__main__':
    #calls
    y = String
    #print fizzBuzz
    y.fizzBuzz(15)
    #string reverse
    text = "reverse it"
    print(y.reverse(text))
    #check if revrse is equal 
    print(y.palindrome("aaba") )
    print(y.palindrome("racecar") )
    #convert to pigLatin
    print(y.pigLatin("aoeuhtn"))
    #Count Vowels
    print(y.countVowels("aoohtnshtnhnhieuaeau"))
    #count Words
    print(y.CountWords("aoeuoeu eouoeu"))
    print(y.CountWords(file= "file.txt"))

