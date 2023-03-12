def main(s):
    """
    A str containing the letter "a" is given. Find the number of letters "a" in this variable.
    Args:
        s: str
    Returns:
        int: answer
    """
    
    return (s.find("a",0,100))
print(main(s="Mobile development"))