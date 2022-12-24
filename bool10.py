from math import sqrt
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    result = sqrt(a) - int(sqrt(a)) == 0
    return result
print(main(9))
print(main(15))