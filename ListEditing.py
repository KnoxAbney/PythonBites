# initialize a few lists of different data types to edit

numbers = [4, 8, 15, 16, 23, 42]
names = ["Elaine", "George", "Jerry", "Cosmo"]
booleans = [True, False, True]
jerry = "Jerry"
nested_lists = [[4, 8], [15, 16], [23, 42]]


# Square every item in a list
def squareIt(nums):
  squares = []

  for num in nums:
    squares.append(num**2)
    
  return squares
    
print(squareIt(numbers))


# add 10 to every item in a list
def plusTen(nums):
  add_ten = []

  for num in nums:
    add_ten.append(num+10)
    
  return add_ten
    
print(plusTen(numbers))


# divide every item in a list by 2
def divideTwo(nums):
  divide_by_two = []

  for num in nums:
    divide_by_two.append(num/2)
    
  return divide_by_two
    
print(divideTwo(numbers))


# determine if a number
def findParity(nums):
  parity = []

  for num in nums:
    parity.append(num%2)
    
  return parity
    
print(findParity(numbers))


# turn a list of names into a greeting
def greet(people):
  greetings = []

  for person in people:
    greetings.append("Hello, " + person)
  
  return greetings

print(greet(names))
  

# find the first character in a list of strings
def findFirstChar(people):
  first_character = []

  for person in people:
    first_character.append(person[0])
  return first_character

print(findFirstChar(names))


# finds the length of each string in a list
def findLength(strings):
  lengths = []

  for string in strings:
    lengths.append(len(string))
  return lengths

print(findLength(names))


# outputs the inverse of each boolean in a list
def findOpposite(variables):
  opposite = []

  for variable in variables:
    opposite.append(not variable)
  return opposite

print(findOpposite(booleans))


# identify if the strings in a list match a given string
def findString(strings,identifier):
  is_same = []

  for string in strings:
    is_same.append(string == identifier)
  return is_same

print(findString(names,jerry))


# multiply the numbers contained in a nested list
def multiply(numbers):
  
  products = [item1*item2 for (item1, item2) in numbers]
  
  return products

print(multiply(nested_lists))
