import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 5, 4, 5]}
df = pd.DataFrame(data)

# Calculate the means of X and Y
mean_x = np.mean(df['X'])
mean_y = np.mean(df['Y'])

# Calculate the slope (m) and intercept (b) of the regression line
numerator = sum((df['X'] - mean_x) * (df['Y'] - mean_y))
denominator = sum((df['X'] - mean_x) ** 2)
m = numerator / denominator
b = mean_y - m * mean_x

# Predict Y values using the regression line
df['Y_pred'] = m * df['X'] + b

# Plot the original data and the regression line
plt.scatter(df['X'], df['Y'], label='Original Data')
plt.plot(df['X'], df['Y_pred'], color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear Regression')
plt.show()

# Print the regression line equation
print(f"Regression Line Equation: Y = {m:.2f}X + {b:.2f}")
