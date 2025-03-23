import math

def calculate_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

radius = 5
height = 10
volume = calculate_volume(radius, height)
print("Volume of a cylinder with radius {} and height {} is {}".format(radius, height, volume))
