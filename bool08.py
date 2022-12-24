def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    answer = a >= 0
    return answer
print(main(-3))
print(main(8))
print(main(0)) 