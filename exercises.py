# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.
'''
def manage_students():
    # your code here
    students = ['sam', 'tina', 'greg']
    first_student = students[0]
    last_student = students[-1]
    return f"first_student: {first_student}, last_student: {last_student}"

# Call the function and print the result
print('Exercise 1:', manage_students())
# '''

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.
foods = 'lettuce1', 'celery2', 'gravy3'
'''
def combine_foods():
    # your code here
    meal = ''
    for item in foods:
        meal += item
    return meal


# Call the function and print the result
print('Exercise 2:', combine_foods())
# '''

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.
'''
def slice_foods():
    # your code here
    last_two = foods[-2:]
    return last_two

# Call the function and print the result
print('Exercise 3:', slice_foods())
# '''

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”
home_town = {
    'city': 'LA',
    'state': 'Hawaii',
    'population': 70,
}
'''
def hometown_info():
    # your code here
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message


# Call the function and print the result
print('Exercise 4:', hometown_info())
# '''

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"
# '''
def list_home_town_items():
    # your code here
    home_town_items = []
    for [key, val] in home_town.items():
        home_town_items.append(f"{key} = {val}")
    return home_town_items


# Call the function and print the result
print('Exercise 5:', list_home_town_items())
# '''
