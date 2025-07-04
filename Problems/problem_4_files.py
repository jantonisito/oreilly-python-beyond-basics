"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""
#from selenium.webdriver.common.devtools.v135.io import close

# from Problems.Solutions.problem_4_files_solution import countries

# Todo: Read data/countries.txt and save all countries
countries_by_letter = {}
with open('data/countries.txt') as file:
    for line in file.readlines():
        country = line.strip()
        # if country[0] not in countries_by_letter:
        #     countries_by_letter[country[0]] = []
        #     countries_by_letter[country[0]].append(country)
        # else:
        #     countries_by_letter[country[0]].append(country)
        # another faster way to do it:
        countries_by_letter.setdefault(country[0], []).append(country)

# Get user to provide a letter
while True:
    letter = input('Number of countries that start with letter (or \'xx\' to exit): ').upper()
    if letter == 'XX':
        break
    if letter in countries_by_letter:
        print(f"The sum was {len(countries_by_letter[letter])}")
    else:
        print(f"No countries start with {letter}")

# Todo: Create text file that lists the countries starting with the letter
with open('data/countries_by_letter.txt', 'w') as file:
    for key in sorted(countries_by_letter.keys()):
        file.write(key + "-------------------------\n")
        for country in countries_by_letter[key]:
            file.write(country + "\n")



# Todo: Print the number of countries that start with the letter
# sum_ = 0
# with open('data/countries.txt') as file:
#     for line in file.readlines():
#         if line.strip()[0] == letter:
#             sum_ += 1
