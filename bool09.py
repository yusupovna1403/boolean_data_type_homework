def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    answer = a > 0 and a - int(a) == 0
    return answer
print(main(3.1))
print(main(-1))
print(main(7))