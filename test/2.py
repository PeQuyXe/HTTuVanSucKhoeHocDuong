import matplotlib.pyplot as plt
import numpy as np

def fuzzy_height(height):
    low = max(0, min(height - 90, 130 - height)) / 40
    medium = max(0, min(height - 120, 150 - height)) / 30
    high = max(0, min(height - 140, 180 - height)) / 40
    return low, medium, high

def fuzzy_weight(weight):
    light = max(0, min(weight - 30, 60 - weight)) / 30
    medium = max(0, min(weight - 25, 80 - weight)) / 35
    heavy = max(0, weight - 50) / 30
    return light, medium, heavy

height_values = np.arange(80, 200, 1)
low_values, medium_values, high_values = zip(*[fuzzy_height(h) for h in height_values])

plt.figure(figsize=(10, 5))
plt.plot(height_values, low_values, label='Low')
plt.plot(height_values, medium_values, label='Medium')
plt.plot(height_values, high_values, label='High')
plt.title('Fuzzy Height')
plt.xlabel('Height')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

weight_values = np.arange(0, 100, 1)
light_values, medium_values, heavy_values = zip(*[fuzzy_weight(w) for w in weight_values])

plt.figure(figsize=(10, 5))
plt.plot(weight_values, light_values, label='Light')
plt.plot(weight_values, medium_values, label='Medium')
plt.plot(weight_values, heavy_values, label='Heavy')
plt.title('Fuzzy Weight')
plt.xlabel('Weight')
plt.ylabel('Membership Value')
plt.legend()
plt.show()
