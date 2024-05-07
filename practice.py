# this is shekars branchA 
# this is gowthams branchB
# this is chitras branchC
# import os
# import sys
# input_file = sys.argv[1]
# word = sys.argv[2]

# def read_file(input_file, word):
#     with open(input_file, 'r') as f:
#         content = (f.read()).split()
#         for line in content:
#             if word in line:
#                 print(line)

# read_file(input_file, word)
#palindrome
import sys  
string = sys.argv[1]
def reverse_string(string):

    r_s = string[::-2] # start : stop : step
    return r_s

print(reverse_string(string))
