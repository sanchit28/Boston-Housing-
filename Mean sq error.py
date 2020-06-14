import matplotlib.pyplot as pt

import numpy as np


from sklearn.metrics import mean_squared_error

#Generate 'n' evenly spaced values from zero to 2  pi radians
n = 200
x = np.linspace(0, 2 * np.pi, n)
sine_values = np.sin(x)

#plot the sin wave
plt.plot(x, sine_values)

#add noise to sine wave
noise = 0.5
noisy_sine_values = sine_values + np.random.uniform(-noise, noise, n)

#plot the noisy values
plt.plot(x, noisy_sine_values, color='r')
plt.plot(x, sine_values, linewidth=3)

#Calculate MSE using equation
error_value = (1/n) * sum(np.power(sine_values - noisy_sine_values, 2))
error_value

#calculate MSE from sklearn library
mean_squared_error(sine_values, noisy_sine_values)