def is_power_of_two(n):
    """
    Check if a number is a power of two.
    
    Args:
        n (int): A positive integer.
        
    Returns:
        bool: True if n is a power of two, False otherwise.
    """
    return n > 0 and (n & -n) == n

def main():
    num = int(input("Enter a number to check if it's a power of two: "))
    print(is_power_of_two(num))

if __name__ == "__main__":
    main()
