class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        return NotImplemented

# Create two instances of the Person class
p1 = Person("John", 30)
p2 = Person("Jane", 25)

# Add the ages of the two Person objects
age_sum = p1 + p2

print(p1)
print(p2)
print(f"The sum of ages is: {age_sum}")
