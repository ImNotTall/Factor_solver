# comments for squares / primes
def get_factors(var_to_factor):
    factor_list = []

    # Iterate up to the square root of the input number
    for item in range(1, int(var_to_factor ** 0.5) + 1):
        # If we divide with no remainder, add to the list
        if var_to_factor % item == 0:
            factor_list.append(item)
            # If the factors are not the same, add the larger factor
            if item != var_to_factor // item:
                factor_list.append(var_to_factor // item)

    factor_list.sort()  # Optionally, you can sort the factors
    return factor_list


# Example usage:
number_to_factor = 12
factors = get_factors(number_to_factor)
print(f"The factors of {number_to_factor} are: {factors}")
