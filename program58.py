def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return result

# Example usage
print(divide_by_zero())