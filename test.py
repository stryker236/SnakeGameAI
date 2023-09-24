import numpy as np
from scipy.stats import norm
import random
import matplotlib.pyplot as plt

def sax_transform(time_series, n_segments, alphabet_size):
    # Calculate breakpoints for the chosen alphabet size
    breakpoints = norm.ppf(np.linspace(0, 1, alphabet_size + 1)[1:-1])

    # Split the time series into segments
    segment_length = len(time_series) // n_segments
    segments = [time_series[i:i+segment_length] for i in range(0, len(time_series), segment_length)]

    # Initialize an empty list to store the symbols
    symbols = []

    # Convert segments to symbols
    for segment in segments:
        mean = np.mean(segment)
        # Find the corresponding symbol based on the mean and breakpoints
        symbol = next((s for s, bp in zip('abcdefghijklmnopqrstuvwxyz', breakpoints) if mean < bp), 'z')
        symbols.append(symbol)

    # Convert the list of symbols to a string
    symbolic_representation = ''.join(symbols)

    return symbolic_representation

# Example usage:´
mu, sigma = 0, 0.1 # mean and standard deviation
time_series = np.random.normal(mu, sigma, 100)
# time_series = [random.uniform(0,2) for i in range(100)]
# time_series = [np.random.normal(mu, sigma, 1000) for i in range(100)]
n_segments = 100
alphabet_size = 50

sax_result = sax_transform(time_series, n_segments, alphabet_size)
print("SAX representation:", sax_result)
plt.plot(time_series)
plt.show()
