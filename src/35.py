def calculate_area(shape):
    if shape == "square":
        side = float(input("Enter the length of the square side: "))
        area = side ** 2
        print(f"The area is {area:.2f}")
    
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area is {area:.2f}")
    
    else:
        print("Invalid shape")
