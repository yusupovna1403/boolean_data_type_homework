def main(a):
    """
    check the following statement "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    result = a % 2 == 0
    return result
print(main(8))
print(main(5))
    