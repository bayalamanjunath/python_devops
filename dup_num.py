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
# import sys  
# string = sys.argv[1]
# def reverse_string(string):

#     r_s = string[::-2] # start : stop : step
#     return r_s

# print(reverse_string(string))

numbers = [1,2,3,4,4,5,5,2,1,6]
duplicate_numbers = []
unique_numbers = set()

for number in numbers:
    if number in unique_numbers:
        duplicate_numbers.append(number)
    else:
        unique_numbers.add(number)
print(unique_numbers)
print(duplicate_numbers)

# top_scores = input().split()
# top_scores = [int(i) for i in top_scores]
# print(top_scores)
# higst_score = -1
# for score in top_scores:
#     if score > higst_score:
#         higst_score = score
# print(f"{higst_score}")


