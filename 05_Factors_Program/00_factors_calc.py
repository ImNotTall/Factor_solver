# Functions go here

# Puts series of symbols at the start and end of text
def statement_generator(text, decoration):
    ends = decoration * 5

    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, "
          "we assume that encoding's is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    return ""


# Checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


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


# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        all_factors = get_factors(var_to_factor)
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares / primes
    if len(all_factors) == 2:
        comment = "{} is a prime number. ".format(var_to_factor)
    elif len(all_factors) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # output factors and comment
    statement_generator(heading, "*")
    print()
    print(all_factors)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
print()
