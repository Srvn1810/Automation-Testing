### Task 1: Create a Python Class called `Circle` with a Constructor
# We need to create a class `Circle` that takes a list as an argument.
# Here's the list: `[10, 501, 22, 37, 100, 999, 87, 351]`.
### Task 2: Create Proper Member Variables
# We'll create a private variable `pi` with the value `3.141`.
### Task 3: Create Methods to Calculate Area and Perimeter

class Circle:
    def __init__(self, radii):
        self.radii = radii
        self.pi = 3.141

    def area(self, radius):
        return self.pi * radius * radius

    def perimeter(self, radius):
        return 2 * self.pi * radius

# Create an instance of Circle with the given list
circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Calculate area and perimeter for each radius in the list
for radius in circle.radii:
    print(f"Radius: {radius}")
    print(f"Area: {circle.area(radius)}")
    print(f"Perimeter: {circle.perimeter(radius)}")
    print("-----")

### Conversion of UML Diagram into Python Class
# Now, I'll visit the provided URL to convert the UML diagram into a Python class.
# [Link to UML Diagram](https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md)
# Here's a conversion of the UML diagram into a Python class:

class TV:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def set_volume(self, volume_level):
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1

# Example usage
tv = TV("Samsung", 55)
tv.turn_on()
tv.set_channel(5)
tv.set_volume(3)
print(f"TV Brand: {tv.brand}, Size: {tv.size} inches, Channel: {tv.channel}, Volume: {tv.volume_level}, On: {tv.on}")


