import math

# Sample dataset
data = [12, 15, 16, 20, 20, 21, 22, 23, 25, 26, 30]

# Calculate the mean
mean = sum(data) / len(data)

# Calculate the mode
def calculate_mode(data):
    freq_dict = {}
    for num in data:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    mode = [key for key, value in freq_dict.items() if value == max(freq_dict.values())]
    return mode

mode = calculate_mode(data)

# Calculate the median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]

# Calculate the standard deviation
mean_deviation = [((x - mean) ** 2) for x in data]
std_dev = math.sqrt(sum(mean_deviation) / len(data))

# Print the results
print(f"Mean: {mean: .2f}")
print(f"Mode: {mode}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev:.2f}")
