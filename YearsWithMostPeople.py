import random as rand
import matplotlib.pyplot as plt


# Creation of a list of the birth and death years of a population
people = []


# Variable to hold the size of the population
population_size = 100

# Loop to pseudo-randomly generate birth and death years for the population
for i in range(population_size):
    birth = rand.randint(1900, 2000)    # Randomly select the birth year from 1900-2000
    death = rand.randint(birth, 2000)   # Randomly choose the year they die from their birth year to 2000
    people.append([birth, death])


# Dictionary to store the number of people alive in a given year initialized at 0
people_alive_by_year = {year: 0 for year in range(1900, 2001)}


# Loop to count the number of people alive in a given year
# Start by looping over the list of people
for person in people:
    for year in range(person[0], person[1]+1):  # For each year that person was alive
        people_alive_by_year[year] += 1         # increase the count of people alive that year


# Find the most people alive in a given year by taking the maximum of the counts
most_people_alive = max(people_alive_by_year.values())


# List of years with the most people alive
years_with_most_people = [year for year in range(1900, 2001) if people_alive_by_year[year] == most_people_alive]


# Create a show a bar graph with the number of people alive each year
plt.bar(people_alive_by_year.keys(), people_alive_by_year.values())
plt.show()