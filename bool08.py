def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    result = a >= 0 and a - int(a) == 0
    return result
print(main(3.1))
print(main(0))
print(main(-1)) 