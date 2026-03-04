def volume_of_box(length, width, height):
    volume = length * width * height
    print(f"The volume of a box with length {length}, width {width}, and height {height} is: {volume}")
    return volume

box_dimensions = (10, 5, 2)
volume_of_box(*box_dimensions)