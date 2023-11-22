# 1. create a python class called circle with constructor which will take a list as an argument for the task.
# the list is [10, 501, 22, 37, 100, 999, 87, 351]

import math
# class Circle:
#     def __init__(self, radius_list):
#         self.radius_list = radius_list
#     def caculate_area(self):
#         areas = [math.pi * r**2 for r in self.radius_list]
#         return areas
#     def calculate_circumference(self):
#         circumferences = [2 * math.pi * r for r in self.radius_list]
#         return circumferences
# radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
# circle_instance = Circle(radius_list)
# areas = circle_instance.calculate_area()
# circumferences = circle_instance.calculate_circumference()
# print("Areas:", areas)
# print("Circumferences:", circumferences)

# 2. Create proper member variables inside the task if required and use them when
# necessary. for example for this task create a class private variable named pi = 3.141

import math

class Circle:
    _pi = 3.141
    def __init__(self, radius_list):
        self._radius_list = radius_list
        self._areas = []
        self._circumferences = []
    def calculate_area(self):
        # Using the private class variable
        self._areas = [self._pi * r**2 for r in self._radius_list]
    def calculate_circumference(self):
        # Using the private class variable
        self._circumferences = [2 * self._pi * r for r in self._radius_list]
    def get_areas(self):
        return self._areas
    def get_circumferences(self):
        return self._circumferences
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

circle_instance.calculate_area()
circle_instance.calculate_circumference()

areas = circle_instance.get_areas()
circumferences = circle_instance.get_circumferences()

print("Areas:", areas)
print("Circumferences:", circumferences)

# 3. from the given list create two class methods area & perimeter
# which will be going to calculate the area & perimeter

import math
class Circle:
    _pi = 3.141
    def __init__(self, radius_list):
        self._radius_list = radius_list
    @classmethod
    def calculate_area(cls, radius):
        # Using the private class variable
        return cls._pi * radius**2
    @classmethod
    def calculate_perimeter(cls, radius):
        # Using the private class variable
        return 2 * cls._pi * radius
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in radius_list:
    area = Circle.calculate_area(radius)
    perimeter = Circle.calculate_perimeter(radius)
    print(f"Radius: {radius}, Area: {area}, Perimeter: {perimeter}")
