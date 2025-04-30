# Find the greatest among three numbers.

def greatestNumber(first, second, third):
    if first > second and first > third:
        print(f"The number {first} is the greatest")
    
    elif second > first and second > third:
        print(f"The number {second} is the greatest")

    else:
        print(f"The number {third} is the greatest")


greatestNumber(1, 2, 3)