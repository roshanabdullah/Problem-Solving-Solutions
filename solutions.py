# Reverse a string
def reverseString(a):
    reversedString = ''
    for char in a:
        reversedString = char + reversedString
    print(reversedString)    
reverseString('abc')

# Get even or odd
def getEvenAndOdd(numbers):
    for number in numbers:
        if(number%2 == 0):
            print("Even numbers are : ", number)
        elif(number%2 != 0):
            print("Odd numbers are : ", number)
            
getEvenAndOdd([2, 4, 6, 3, 10])

#sort numbers
def sortNumbers(numbers):
    print(sorted(numbers))
        
sortNumbers([1, 5, 10, 0, 10, 8])


# Find repeated numbers
def findRepeatedNumber(numbers):
    seen = set()
    repeated = set()
    
    for number in numbers:
        if(number in seen):
            if number not in repeated:
                print(number)
                repeated.add(number)
        else:
            seen.add(number)
    
findRepeatedNumber([1, 2, 3, 3, 3, 2, 2])


Find the Palindrome of a string
def checkPalindromeOfString(s):
    reversed_string=""
    original_string=""
    
    for char in s:
        reversed_string=char+reversed_string
        
    original_string="".join(s)
    if(original_string == reversed_string):
        print(f"{original_string} is a palindrome")
    else:
        print(f"{original_string} is not a palindrome")
    
checkPalindromeOfString(['a', 'b'])

# Calculate total number of numerical digits in a string or total characters
def calNumOfNumericalDigitsOrCharactersInString(s):
    numericalCount = 0;
    characterCount = 0;
    for char in s:
        if char.isdigit():
            numericalCount += 1
        characterCount = characterCount + 1
        
calNumOfNumericalDigitsOrCharactersInString(['a','b','c', '1', '2', '.'])
