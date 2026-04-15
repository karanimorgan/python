class AreaOfShapes:
    def area(self, **measurements):
        raise NotImplementedError("subclasses must implement this method")

class circle(AreaOfShapes):
    def area(self, **measurements):
        radius = measurements.get("radius")
        if radius is not None:
            return 3.14 * radius ** 2
        else:
            raise ValueError("Missing 'radius' for circle area calculation")
        
class Rectangle(AreaOfShapes):
    def area(self, **measurements):
        length = measurements.get("length")
        width = measurements.get("width")
        if length is not None and width is not None:
            return length * width
        else:
            raise ValueError("Missing 'length' or 'width' for rectangle area calculation")
        
class Triangle(AreaOfShapes):
    def area(self, **measurements):
        base = measurements.get("base")
        height = measurements.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            raise ValueError("Missing 'base' or 'height' for triangle area calculation")
        
shapes = [circle(), Rectangle(), Triangle()]

for shape in shapes:
    if isinstance(shape, circle):
        print(f"Area of circle with radius 5:{shape.area(radius=5)}")
    elif isinstance(shape, Rectangle):
        print(f"Area of Rectangle with length 4 and width 6: {shape.area(length=4,width=6)}")
    elif isinstance(shape, Triangle):
        print(f"Area of Triangle with base 3 and height 7: {shape.area(base=3,height=7)}")
        