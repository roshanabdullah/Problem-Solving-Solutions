# reverse characters format 1 using string
def reverseChar(s):
    reversed_String = ""
    for char in s:
        reversed_String = char + reversed_String
    return reversed_String
print(reverseChar(['a', 'b', 'c']))

# reverse characters format 2 using list 
def reverseChar(s):
    reversed_String = []
    for char in s:
        reversed_String.insert(0, char)
    return reversed_String

print(reverseChar(['a', 'b', 'c']))

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

# Finding min and maximum number
# function method
def findMaxNum(s):
    print(max(s))
    print(min(s))
    
    
findMaxNum([1, 2, 3,2])

# vanilla method
def findMaxNum(s):
    
    max_num = s[0]
    min_num = s[0]
    for num in s[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
            
    print(max_num)
    print(min_num)
        
findMaxNum([5, 2, 3])


# quick sort alogorithm to get ascending order 
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
        
print(quicksort([3, 2, 1]))


# quick sort for descending
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        return quicksort(left) + middle + quicksort(right)

print(quicksort([1, 56, 3]))

# sort array in ascending order and then find the middle no
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
    
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
       
    
numbers = [7,6,4,2,8,5]   
sorted_list = quicksort(numbers)

def findSortedMiddleNum(num):
    middle_index = len(num) // 2
    # If the list has an odd number of elements, the middle element is the one at the middle index
    if len(num) % 2 == 1:
        middle_number = num[middle_index]
    # If the list has an even number of elements, the middle element is the average of the two middle elements
    elif len(num) % 2 == 0:
        middle_number = (num[middle_index - 1] + num[middle_index]) / 2
        
    print(middle_number)
    
findSortedMiddleNum(sorted_list)


# Finding anagrams of strings
def findAnegrams(s1, s2):
    str1 = "".join(s1)
    str2 = "".join(s2)
    
    if len(str1) != len(str2):
        print("string are not anegram due to unmatching length")
    else:
        if sorted(str1) == sorted(str2):
            print("anegrams")
        else:
            print("not anegram")
    
findAnegrams(['a', 'b', 'c'], ['c', 'b', 'a'])
