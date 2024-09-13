# A guessing game

This repository contains two scripts that you can run from the command-line. If you want to be the one guessing at the real value, you use

```sh
> python3 src/player-guessing.py
```


## Below or above

- Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem.

1. Starts with guessing lowest possible value and increments through all valid values until the end of possible values, thereby having a termination either with correct value guess or no more valid values.
2. Same as 1. but from highest possible value and decrementing through all valid values.
3. Guesses at the middle of the current working list, if guess is wrong then makes a sublist based on the answer that will include the correct value. As the guess always guesses at the middle of the working list it finds the correct value as the value is always included in the working list.

- Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the correct number first is ranked highest, and the algorithm most likely to get the right number last is rated lowest. Justify your answer.

Strategy 3 > strategy 1 and 2. Worst case scenario 3. will have half as many steps as 1. and 2.
