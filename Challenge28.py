# Write a function that takes a list of numbers and returns only the even numbers:

def filter_even(nums):
    # your code here
    for num in nums:
      if num % 2==0:
        print(num)
      
nums = [2, 4, 5, 6, 8, 10]

filter_even(nums)
