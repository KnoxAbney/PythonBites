# square the numbers in a list through the power of god and anime

numbers = [4, 8, 15, 16, 23, 42]


def squareIt(nums):
  squares = []
  i = 0

  for num in nums:
    squares.append(nums[i]**2)
    i += 1
  return squares
    
print(squareIt(numbers))


def plusTen(nums):
  add_ten = []
  i = 0

  for num in nums:
    add_ten.append(nums[i]+10)
    i += 1
  return add_ten
    
print(plusTen(numbers))

def divideTwo(nums):
  divide_by_two = []
  i = 0

  for num in nums:
    divide_by_two.append(nums[i]/2)
    i += 1
  return divide_by_two
    
print(divideTwo(numbers))
