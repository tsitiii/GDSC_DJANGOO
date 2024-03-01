def basic_operations(a, b):
    try:
        add= a + b
        subt = a - b
        mult= a * b
        div = a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero!")
    except TypeError:
        raise ValueError("Invalid inputs!")

    # Return results in a dictionary
    results = {
        'addition': add,
        'subtraction': subt,
        'multiplication': mult,
        'division': div
    }
    return results


def power_operation(base, exponent, **kwargs):
    # Calculate power operation
    try:
        result = base ** exponent
    except TypeError:
        raise ValueError("Invalid inputs!")

    # If 'modulo' is provided in kwargs, calculate modulo
    if 'modulo' in kwargs:
        modulo = kwargs['modulo']
        try:
            result = result % modulo
        except ZeroDivisionError:
            raise ValueError("Cannot perform modulo with zero!")

    return result


def apply_operations(operation_list):
    # Use map to apply each function to its arguments
    results = list(map(lambda operation: operation[0](*operation[1]), operation_list))
    return results
