## Extra Credit Explanation
*(This document was attached to the `elves.py` program which was printed out and turned in.)*

On my first attempt, I attempted to solve the problem with pen and paper, drawing a table for the information. However, after attempting to find a solution for 15 minutes, I decided that writing a computer program would be easier and less time consuming.

This task wasn’t as easy as I initially thought, as I quickly came to realize. My first problem was finding a way to represent the data. I thought about using some sort of dictionary to match elves to values, but realized that the data type was difficult to work with. I also thought about using a list for each elf, trying that out until I settled on a 3 layer nested list. Using some built in Python modules, I could easily generate all possible combinations for each elf, and then created a generator to combine the combinations into a complete set of all elves. I tested the code to see if it would work… and it didn’t.

After some debugging, I realized that the generators for calculating the combinations of each elf stopped when they got to the end, so I had them restart after each loop in order to get the full set of elf combinations. With that finished, it was time to manually program in each requirement on the sheet. This had to be done in a specific way to optimize the search, since there were so many combinations. More common checks would be performed first, so as to not waste time checking things that don’t work. Originally, each run would take up to 10 minutes to finish, so I decided to use some logic to manually shrink the search space. Using logical deductions, I shrunk the search space as much as I could, to 6 million combinations from 976 billion. Things were running a lot faster now, taking only about 30 seconds to complete. 

However, it wasn’t outputting any results. I started to add print() statements to see what the code was doing, blocking out different sections of code, and started debugging. This part by far took the longest time, probably at least 45 minutes and up to an hour. By the end of this, I had spent almost 2 hours staring at the computer, only to realize that the problem was so obviously simple I was mad at myself. In one of the checks, I was checking against the word “train”, however, my data used the plural form “trains”. That one simple “s” cost me a whole hour of my life, contributing to the many annoyances in trying to tell a computer what to do. Finally, after some cleanup, commenting, and further optimization, it was complete. The program could successfully output the correct answer after just around 20 seconds. Hurray!

While programming may take a long time initially, the benefits of using such a program lies in scalability: doing this by hand may be quicker, but you’ll need to spend the same time again if the rules and problems change. However, with the program, just tweaking the checks and input data can get you the results you want much faster, even with a higher initial cost.

After doing all this, I asked you if this was a valid way to solve the problem, and the answer was that pen and paper was preferred. :(

Anyway, I just used a similar strategy as my first attempt, only with a different chart including all possible values for that cell, which I could slowly eliminate one by one. This final attempt gave me the correct answer in about a quarter of the time spent programming, ~10-15 minutes. 

¯\_(ツ)_/¯
