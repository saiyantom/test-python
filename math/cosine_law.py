import math

a = int(input("Enter the length of side A: "))
b = int(input("Enter the length of side B: "))
c = int(input("Enter the length of side C: "))

print(f'Side A/B/C: {a}|{b}|{c}')

angle_a = math.acos(((b ** 2)+(c ** 2)-(a ** 2) ) / (2*b*c) ) * 180/math.pi
angle_b = math.acos(((a ** 2)+(c ** 2)-(b ** 2) ) / (2*a*c) ) * 180/math.pi
angle_c = math.acos(((a ** 2)+(b ** 2)-(c ** 2) ) / (2*a*b) ) * 180/math.pi

print(f'Angle A: {angle_a}')
print(f'Angle B: {angle_b}')
print(f'Angle C: {angle_c}')
