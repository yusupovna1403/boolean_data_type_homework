def main(b):
    """
    check the following statement "The variable "b" is positive"
    Args:
        b: int
    Returns:
        bool
    """
    answer = b >= 0
    return answer
print(main(-3))
print(main(8))