import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt

# 1. NumPy: Create array and calculate mean
array = np.arange(1, 11)  # Numbers 1 to 10
mean_value = np.mean(array)
print("1️⃣ NumPy Array:", array)
print("   Mean:", mean_value)

# 2. Pandas: Create a small DataFrame and show summary stats
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [88, 92, 85]
}
df = pd.DataFrame(data)
print("\n2️⃣ Pandas DataFrame:\n", df)
print("\n   Summary Statistics:\n", df.describe())

# 3. Requests: Fetch data from a public API
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_price = bitcoin_data['bpi']['USD']['rate']
    print("\n3️⃣ Current Bitcoin Price (USD):", usd_price)
else:
    print("\n3️⃣ Failed to fetch API data.")

# 4. Matplotlib: Plot a line graph
numbers = [1, 3, 5, 7, 9]
plt.plot(numbers, marker='o', linestyle='-', color='green')
plt.title("4️⃣ Simple Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
