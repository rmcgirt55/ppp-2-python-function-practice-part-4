# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(arg1, arg2, arg3):
    maximum = max(arg1, arg2, arg3)
    print(f"The max # among {arg1}, {arg2}, and {arg3} is {maximum}")

max_num(1, 2, 3)


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(random_list):
    result = 1
    for num in random_list:
        result *= num
    print(f"After multiplying all the numbers in {random_list}, the result is {result}")

num_list = {1, 2, 3}
mult_list(num_list)


# Write a Python function called rev_string() to reverse a string.
def rev_string(input):
    reversed_string = input[::-1]
    print(reversed_string)

rev_string("hello")


"""
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
"""
def num_within(num, start_range, end_range):
    if start_range <= num <= end_range:
        print("True")
    else:
        print("False")

num_within(12, 10, 100)
num_within(200, 500, 1000)


"""
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle
The function accepts the number n, the number of rows to print
"""
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)