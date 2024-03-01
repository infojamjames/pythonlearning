import matplotlib.pyplot as plt

# Example data: Monthly average temperatures (°C)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [4, 5, 8, 12, 16, 20, 22, 21, 18, 13, 8, 5]

# Creating the plot
plt.figure(figsize=(10, 6))  # Optional: Specifies the figure size
plt.plot(months, temperatures, marker='o', linestyle='-', color='b')

# Adding title and labels
plt.title('Monthly Average Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Optional: Adding a grid
plt.grid(True)

# Display the plot
plt.show()
