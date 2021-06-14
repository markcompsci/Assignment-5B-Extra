DIAMETER = input("Welcome to the area and circumference calculator!\n\nEnter a diameter length in cm: ")
PI = 3.14159
RADIUS = int(DIAMETER) / 2
result = ""

# Basically creating my own .toFixed() in Python.
# It splits the integer from the float, cuts off excess digits from the float,
# then, concatenates them together 

def fixed(num):
  num = str(num)
  integer = num.split(".")[0]
  decimal = num.split(".")[1]
  return float(f"{integer}.{decimal[:3]}")

result += f"The area is {fixed(PI * (RADIUS ** 2))}cm\n\n"

result += f"The circumference is {fixed(2 * PI * RADIUS)}cm"

print(result)