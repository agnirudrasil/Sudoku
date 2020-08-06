# Sudoku

![Logo](https://github.com/AgnirudraSil/Sudoku/blob/master/icon.png)


This project uses the pygame and Tkinter libraries.

You have to install them first, by running the following commands:

> pip3 install pygame

> pip3 install tkinter

Just paste the commands, one by one, in your terminal, or just type them out.

Be sure to install all the fonts provided in the `fonts` folder, or you **will get errors**.

Then run the `gui_own.py` file

# Controls:

* <kbd>Left-Click</kbd> enter number in a grid

* <kbd>Right-Click</kbd> activate pencil

* <kbd>Tab</kbd> use hint

* <kbd>Del</kbd> delete number or pencil marks in the cell

* <kbd>Space</kbd> let the AI solve the puzzle for you

# Note

* This program uses the [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) to generate and solve the puzzles. On rare ocassions, the AI may fail, or the puzzle generation can take a while.
* Everytime, when the AI reaches the last cell, it will take a while to place a number. That is because of how backtracking works😥
