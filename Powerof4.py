def istothePowerofFour(n):
    if n <= 0:
        return False
    
    # Check if n is a power of 2 first
    if (n & (n - 1)) != 0:
        return False
    
    # Check if the only set bit is at an even position (power of 4)
    return (n % 3 == 1)

num = int(input("Enter a number: "))

if istothePowerofFour(num):
    print(num, "is  a power of 4")
else:
    print(num, "is NOT a power of 4")