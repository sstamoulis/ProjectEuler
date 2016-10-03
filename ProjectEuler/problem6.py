# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
n=100
nums = range(1,n+1)
squares = [x**2 for x in nums]
sumOfSquares = sum(squares)
squareOfSum = sum(nums)**2
print("{} - {} = {}".format(squareOfSum,sumOfSquares,squareOfSum-sumOfSquares))