import math
oil_max = 0.3826834
oil_min = -0.9238795
alpha = math.degrees(abs(math.asin(oil_max)) + abs(math.asin(oil_min)))
print(alpha)
sector_s = 2 * (alpha * math.pi / 360)
triang_s = math.sin(360 - 2 * alpha)

print(triang_s)
fill_factor = (sector_s + triang_s)/(math.pi)
print(fill_factor)