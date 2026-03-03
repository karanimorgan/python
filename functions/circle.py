def area_of_circle(diameter, pi = 3.142):
    # area = pi * radius ** 2
    radius = diameter/2
    area = pi * radius ** 2
    return area
if __name__ == "__main__":
    diameter = 10
    area = area_of_circle(diameter)
    print(f"The area of a circle with diameter {diameter} is: {area}")

    diameter = 21
    area = area_of_circle(diameter)
    print(f"The area of a circle with diameter {diameter} is: {area}")