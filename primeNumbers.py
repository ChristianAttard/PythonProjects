# this program displays the prime numbers from 1 to 50
# first for loop to iterate a loop between 1 and 50
for Number in range(1, 50):
    # count will return the number of times an object appears
    count = 0
    # second for loop to check if that number can be divided or not
    # if the number returns true, therefore divisible, the count is incremented,
    # break statement will skip that number
    for i in range(2, (Number // 2 + 1)):
        if Number % i == 0:
            count = count + 1
            break
    # if statement to check if the count is 0, and the given number is not equal to 1.
    # If it is true, the prime number will be printed
    if count == 0 and Number != 1:
        # print an integer, %d is an operator
        print(" %d" % Number, end='  ')

# # asking the user to input the minimum and maximum range values
# # storing both inputs as int minimum and maximum variables
# minimum = int(input(" Please Enter the Minimum Value: "))
# maximum = int(input(" Please Enter the Maximum Value: "))
#
# for Number in range(minimum, maximum + 1):
#     count = 0
#     for i in range(2, (Number // 2 + 1)):
#         if Number % i == 0:
#             count = count + 1
#             break
#
#     if count == 0 and Number != 1:
#         print(" %d" % Number, end='  ')

