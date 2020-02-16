## ATDP Academic Product
*(This was submitted as an Academic Product for a summer camp I applied to. This gives more context for the problem and my thought process as I worked through it.)*

This is a Python program I wrote in an attempt to solve an extra credit homework problem assigned by my math teacher. The problem was a holiday-themed logic puzzle in the form of a poem. The original assigned problem is attached below.

To solve this, I decided to write a Python program to try all the possible combinations of elves, toys, clothing colors, and amounts to see which one satisfied all the conditions. I thought it would be easier and less time-consuming than doing it by hand, but I quickly realized that it was not the case.

My first problem was finding a way to represent the data. I thought about using some sort of dictionary to match elves to values but realized that the data type was difficult to work with, especially when trying to generate the combinations. I also thought about using a list for each elf, trying that out until I settled on a 3 layer nested list (lines 10-14). Using some built-in Python modules, I could easily generate all possible combinations for each elf and then created a Python generator to combine the combinations into a complete set of all elves. I tested the code to see if it would work… and it didn’t.

After some debugging, I realized that the generators for calculating the combinations of each elf stopped when they got to the end, so I had them restart after each loop in order to get the full set of elf combinations (lines 31-34). With that finished, it was time to manually program in each requirement on the sheet. This had to be done in a specific way to optimize the search since there were so many combinations. More common checks would be performed first, so as to not waste time checking things that don’t work. Originally, each run would take up to 10 minutes to finish, and when using the full search space (ignoring all the clues), it didn’t finish even when given 40 minutes. To make it run faster, I decided to use some logic to manually shrink the search space. Using only very obvious logical eliminations, I shrunk the search space as much as I could, down to 6 million combinations from 976 billion (lines 10-14). Things were running a lot faster now, taking only about 30 seconds to complete. 

However, it wasn’t outputting any results. I started to add print() statements to see what the code was doing, blocked out different sections of code, and started debugging. This part by far took the longest time, probably at least 45 minutes and up to an hour. Once I was convinced that the generator wasn’t the problem, my debugging strategy was to test each check by commenting out each check one by one to see which check was filtering out all the results.

By the end of this, I had spent almost 2 hours staring at the computer, only to realize that the problem was so obviously simple I became mad at myself. In one of the checks, I was checking against the word “train” (line 55), however, my data used the plural form “trains”. That one simple “s” cost me a whole hour of my life, contributing to the many annoyances in trying to tell a computer what to do. Finally, after some cleanup, commenting, and further optimization, it was complete. The program could successfully output the correct answer after just around 10-20 seconds. Hurray!

While programming may take a long time initially, the benefits of using such a program lies in scalability: doing this by hand may be quicker, but you’ll need to spend the same time again if the rules and problems change. However, with a computer program, just tweaking the checks and input data can get you the results you want much faster, even with a higher initial cost.

After doing all this, I asked my math teacher if this was a valid way to solve the problem, and the answer was that pen and paper were preferred :(

Anyway, I still wanted to try solving the problem by hand, so I just used a grid of elves and categories with all possible values for each cell written in, which I could slowly eliminate one by one. This final attempt gave me the correct answer in about an eighth of the time I spent programming, ~10-15 minutes. 

Oh well. ¯\_(ツ)_/¯
