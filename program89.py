def print_even_index_chars(input_string):
    # Extract characters at even indexes
    result = input_string[::2]
    print(result)

# Accept input from the console
input_string = input("Enter a string: ")
print_even_index_chars(input_string)