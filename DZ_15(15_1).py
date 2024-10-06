class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_square(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.get_square() == other.get_square()
    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)
    def __mul__(self, n):
        new_area = self.get_square() * n
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def __hash__(self):
        return hash((self.width, self.height))

# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

# Перевірка площ
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

# Перевірка додавання двох прямокутників
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print(r3)  # Rectangle(width=2, height=13.0)

# Перевірка множення прямокутника на число
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)  # Rectangle(width=2, height=16.0)

# Перевірка порівняння двох прямокутників за площею
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
