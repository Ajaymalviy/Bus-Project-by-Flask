import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

# Assuming "cars.txt" is a CSV file with a similar structure to the R example
file_path = "C:/path/to/cars.txt"

# Read the CSV file into a DataFrame
cars = pd.read_csv(file_path, dtype=str)  # Use dtype=str to prevent automatic conversion to categorical

# Display the first seven records in the DataFrame
print(cars.head(7))

# Assuming "cars" is the DataFrame you previously read from the CSV file

# Create a subset of "cars" with records 1 to 5 and variables 1, 3, 4, and 8
cars_tiny = cars.iloc[0:5, [0, 2, 3, 7]]

# Display the resulting subset
print(cars_tiny)



# Assuming "cars_tiny" is the DataFrame you previously created

# Replace missing values in the specified positions with constants
cars_tiny.iloc[1, 1] = 0
cars_tiny.iloc[3, 3] = "Missing"

# Display the resulting DataFrame
print(cars_tiny)


# Replace the missing value with the field mean or mode

# Assuming "cars_tiny" is the DataFrame you previously created

# Recreate the missing value table
cars_tiny.iloc[1, 1] = cars_tiny.iloc[3, 3] = pd.NA

# Replace cars_tiny[1, 1] with the mean of 'cubicinches'
cars_tiny.iloc[1, 1] = cars_tiny['cubicinches'].mean()

# Replace cars_tiny[3, 3] with the mode of 'brand'
our_mode = cars_tiny['brand'].mode().iloc[0]
cars_tiny.iloc[3, 3] = our_mode

# Display the resulting DataFrame
print(cars_tiny)

# Replace missing values with a value generated at random from the observed distribution

# Assuming "cars_tiny" is the DataFrame you previously created

# Recreate the missing value table
cars_tiny.iloc[1, 1] = cars_tiny.iloc[3, 3] = pd.NA

# Generate random observations from observed distribution
obs_brand = np.random.choice(cars_tiny['brand'].dropna(), 1)[0]
obs_cubicinches = np.random.choice(cars_tiny['cubicinches'].dropna(), 1)[0]

# Replace the missing values
cars_tiny.iloc[1, 1] = obs_cubicinches
cars_tiny.iloc[3, 3] = obs_brand

# Display the resulting DataFrame
print(cars_tiny)



# Assuming "cars" is the DataFrame you previously read from the CSV file

# Five-number summary with mean
five_num_summary = {
    'Min': np.min(cars['weight']),
    '25th Percentile': np.percentile(cars['weight'], 25),
    'Median': np.median(cars['weight']),
    '75th Percentile': np.percentile(cars['weight'], 75),
    'Max': np.max(cars['weight']),
    'Mean': np.mean(cars['weight'])
}

# Count
count_weight = len(cars['weight'])

# Display the results
print("Five Number Summary with Mean:")
print(five_num_summary)
print("\nCount of 'weight' column:", count_weight)





# Assuming "cars" is the DataFrame you previously read from the CSV file

# Min-Max Normalization
min_max_normalized_weight = (cars['weight'] - np.min(cars['weight'])) / (np.max(cars['weight']) - np.min(cars['weight']))

# Display Min-Max Normalized 'weight'
print("Min-Max Normalized 'weight':")
print(min_max_normalized_weight)

# Z-score Normalization
zscore_normalized_weight = (cars['weight'] - np.mean(cars['weight'])) / np.std(cars['weight'])

# Display Z-score Normalized 'weight'
print("\nZ-score Normalized 'weight':")
print(zscore_normalized_weight)


# Assuming "cars2.txt" is the CSV file containing the 'weight' column
file_path = "C:/path/to/cars2.txt"
cars2 = pd.read_csv(file_path)

# Set up the plot area
plt.figure(figsize=(8, 6))

# Create the histogram
plt.hist(cars2['weight'], bins=30, range=(0, 5000), color='blue', edgecolor='black')

# Customize the plot
plt.xlabel('Weight')
plt.ylabel('Counts')
plt.title('Histogram of Car Weights')
plt.ylim(0, 40)
plt.grid(True)

# Show the plot
plt.show()


# Assuming "cars2.txt" is the CSV file containing the 'weight' and 'mpg' columns
file_path = "C:/path/to/cars2.txt"
cars2 = pd.read_csv(file_path)

# Set up the plot area
plt.figure(figsize=(8, 6))

# Create the scatterplot
plt.scatter(cars2['weight'], cars2['mpg'], color='blue', marker='o', label='Blue Circles')

# Add open black circles
plt.scatter(cars2['weight'], cars2['mpg'], color='black', marker='o', label='Black Circles', edgecolors='black')

# Customize the plot
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('Scatterplot of MPG by Weight')
plt.xlim(0, 5000)
plt.ylim(0, 600)
plt.legend()

# Show the plot
plt.show()
