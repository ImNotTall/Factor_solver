# Functions Go Here

import math


# Puts series of symbols at start and end of text


def statement_generator(text, decoration):
    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print("This program is created to show you (the user) the factors of a number that you enter")
    print()
    print("Complete as many calculations as necessary,")
    print("Pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# checks input is a number more than a given value


# gets factors, returns a sorted list.
def num_check(question, low, high):
    while True:

        error = f"Please enter a number between {low} and {high}"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if low <= response <= high:
                return response

            # outputs error if input is invalid
            else:
                print(error)

        except ValueError:
            print("Ooops, you did not enter an integer!")


def get_factors(to_factor):
    var_factor_list = []
    sqrt_num = int(math.sqrt(to_factor))

    for item in range(1, sqrt_num + 1):
        if to_factor % item == 0:
            var_factor_list.append(item)

            # find the second factor in the pair
            partner = to_factor // item

            # if the factor is not already in the list, add it
            if partner not in var_factor_list:
                var_factor_list.append(partner)

    return sorted(var_factor_list)


# Main Routine goes here.

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not opened the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored.
    num_factors = num_check("Number to be factored: ", 1, 200)

    if num_factors != 1:
        factor_list = get_factors(num_factors)
        print("list length", len(factor_list))
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself! :)"

    # comments for squares / primes.
    if len(factor_list) == 2:
        comment = "{} is a prime number".format(num_factors)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(num_factors)

    # Generate Heading
    if num_factors == 1:
        heading = "One is special..."
    else:
        heading = "Factors of {}".format(num_factors)

    # output factors and comment
    statement_generator(heading, "*")
    print()
    print("factor list", factor_list)
    print(comment)
    print()
    keep_going = input("Press <enter> to continue or any key to quit: ")
    print()

print()
print("Thank you for using this Factor Calculator!")
print()
