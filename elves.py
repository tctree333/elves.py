## elves.py | Python program to brute force Ms. Cha's winter break extra credit logic problem
## By Tomi Chen, Dec. 20, 2019
 
import time # imports a time module to get current time
start = time.time() # start time to calculate time elapsed
import itertools # imports a module to calculate combinations
 
# use logic to reduce search space to 6,096,384 from 976,562,500,000 combinations
# elf data, represented by a 3-dimensional matrix (elf, category, value)
data = [[["Cher"], ["blue", "yellow", "green"], ["trains", "balls"], [4, 6, 7, 8, 9, 10, 11]],
       [["Johnny"], ["blue", "red", "yellow", "green"], ["racing cars"], [3, 4, 6, 7, 8, 9, 10, 11]],
       [["Jane"], ["blue", "red", "yellow"], [ "sleds", "trains", "balls"], [5]],
       [["Sue"], ["blue", "red", "yellow"], ["sleds", "trains", "spinning toys", "balls"], [9, 12]],
       [["Marcia"], ["orange"], [ "sleds", "spinning toys", "balls"], [6, 7, 8, 9, 10, 11, 12]]]


'''data = [[["Cher"],  ["red", "orange", "yellow", "green", "blue"], ["racing cars", "sleds", "trains", "spinning toys", "balls"], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
       [["Johnny"], ["red", "orange", "yellow", "green", "blue"], ["racing cars"], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
       [["Jane"],   ["red", "orange", "yellow", "green", "blue"], ["racing cars", "sleds", "trains", "spinning toys", "balls"], [5]],
       [["Sue"],    ["red", "orange", "yellow", "green", "blue"], ["racing cars", "sleds", "trains", "spinning toys", "balls"], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
       [["Marcia"], ["orange"], ["racing cars", "sleds", "trains", "spinning toys", "balls"], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]
'''

# create a generator that outputs all possible elf/color/toy/number combinations, one at a time
def board_gen():
   # create a list for each elf containing all possible combinations for that elf
   cher = itertools.product(*data[0])
   johnny = itertools.product(*data[1])
   jane = itertools.product(*data[2])
   sue = itertools.product(*data[3])
   marcia = itertools.product(*data[4])
   # loop through each possible combinations of elves, output as a 2-D matrix (elf, category)
   for a in cher:
       for b in johnny:
           for c in jane:
               for d in sue:
                   for e in marcia:
                       yield list(map(list, [a, b, c, d, e]))
                   marcia = itertools.product(*data[4])
               sue = itertools.product(*data[3])
           jane = itertools.product(*data[2])
       johnny = itertools.product(*data[1])
 
b = board_gen()
results = []
 
# loop through each matrix
for board in b:
   # check for color/toy/number uniqueness (26,390 combinations satisfy)
   if len(set([board[0][3], board[1][3], board[2][3], board[3][3], board[4][3]])) == 5:
       if len(set([board[0][2], board[1][2], board[2][2], board[3][2], board[4][2]])) == 5:
           if len(set([board[0][1], board[1][1], board[2][1], board[3][1], board[4][1]])) == 5:
               total_gifts = []
               spin = []
               for elf in board:
                   # loop through each elf
                   if elf[1] == "red" and elf[3] != (board[0][3] - 1):
                       # check if elf in red made one less than Cher
                       break # exits loop if check fails
                   if elf[2] == "sleds" and elf[3] != (board[0][3] + 1):
                       # check if elf who made sleds made one more than Cher
                       break # exits loop if check fails
                   if elf[1] == "yellow" and elf[2] != "trains":
                       # check if the yellow elf made trains
                       break # exits loop if check fails
                   if elf[1] == "green" and elf[3] != (board[3][3] / 3):
                       # check if elf in green made 1/3 of Sue
                       break # exits loop if check fails
                   if elf[2] == "spinning toys":
                       spin = elf
                   total_gifts.append(elf[3])
               else:
                   if sum(total_gifts) == 30:
                       # check if there are 30 toys in total
                       if max(total_gifts) == spin[3]:
                           # check if the elf who made spinning toys made the most
                           results.append(board) # log the result if all checks pass
 
end = time.time() # end time to calculate time elapsed
# print results out
print(f"# of results: {len(results)}")
print(f"time elapsed: {end-start} sec")
print(f"result: {results[0]}")
 
# # of results: 1
# time elapsed: 21.654051065444946 sec
# result:
# [['Cher', 'yellow', 'trains', 6],
# ['Johnny', 'green', 'racing cars', 3],
# ['Jane', 'red', 'balls', 5],
# ['Sue', 'blue', 'spinning toys', 9],
# ['Marcia', 'orange', 'sleds', 7]]
