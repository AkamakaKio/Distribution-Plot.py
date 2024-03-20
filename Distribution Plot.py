import numpy as np
import matplotlib.pyplot as plt

# Example data for a normal distribution
mu = 0
sigma = 1
data = np.random.normal(mu, sigma, 1000)

# Plot the probability distribution
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')
plt.title('Probability Distribution Plot (Normal Distribution)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
