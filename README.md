# Determining the year(s) with the most people alive from a dataset of birth and death years

A short program to determine the years with the largest number of people alive from a dataset of peoples' years of birth and death.  The 
years were restricted to be between 1900 and 2000 inclusive.

For this project I chose to use Python.  I started by randomly generating a list of pairs of years to represent the birth and death years 
of a list of people.  I used the the pseudo-random number generator package 'random' that is built into Python.  After generating that list I created a Python dictionary (a hashmap in other languages) to store the number of people alive in a given year.  I initialized it as a dictionary with the years 1900 to 2000 as the keys, and 0 for the values.  I then looped through the list of people and incremented the values in the dictionary for each year they were alive.  I then took the maximum from the list of values in the dictionary, and then listed the keys that matched the maximum value.  That list of keys would then be the year(s) with the most living people in the range 1900 to 2000.

To see (and run) the Python script that does this go to the file [YearsWithMostPeople.py](https://github.com/mmh3719/YearsWithMostPeople/blob/master/YearsWithMostPeople.py) 
(if you don't have matplotlib you can simply comment out the import and the last two lines of code).

To see the dataset, the resulting year(s), and a bar chart showing the number of people alive in a given year without needing to run any 
code, go to the file [YearsWithMostLivingPeople.ipynb](https://github.com/mmh3719/YearsWithMostPeople/blob/master/YearsWithMostLivingPeople.ipynb) 
(this is a Jupyter notebook that lets you modify and display results from snippets of code).
