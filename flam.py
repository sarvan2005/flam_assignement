import numpy as np
import pandas as pd
import math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\velch\Downloads\xy_data.csv")
x_observed = df["x"].values
y_observed = df["y"].values
N = len(df)

t = np.linspace(6, 60, N)

def compute_curve(parameters, t_value):
    theta, M, X = parameters

    expo = np.exp(M * np.abs(t_value))
    sin03t = np.sin(0.3 * t_value)

    x = t_value * np.cos(theta) - expo * sin03t * np.sin(theta) + X
    y = 42 + t_value * np.sin(theta) + expo * sin03t * np.cos(theta)

    return x, y

def distance_objective(parameters):
    x_predicted, y_predicted = compute_curve(parameters, t)
    return np.sum(np.sqrt((x_predicted - x_observed)**2 + (y_predicted - y_observed)**2))

result = minimize(
    distance_objective,
    x0=[0.5, 0.0, 50],             
    method="Powell",               
    bounds=[(0, math.radians(50)), (-0.05, 0.05), (0, 100)]
)

theta_optimized_value, M_optimized_value, X_optimized_value = result.x

x_predicted, y_predicted = compute_curve(result.x, t)
residuals = np.sqrt((x_predicted - x_observed)**2 + (y_predicted - y_observed)**2)

print("\n----- FINAL RESULT -----")
print("theta (degrees):", math.degrees(theta_optimized_value))
print("M:", M_optimized_value)
print("X:", X_optimized_value)
print("Total L1 Distance:", np.sum(residuals))


plt.figure(figsize=(8,6))
plt.scatter(x_observed, y_observed, label="observed Data", s=8)
plt.plot(x_predicted, y_predicted, label="Fitted Curve", linewidth=2)
plt.legend()
plt.grid()
plt.show()
