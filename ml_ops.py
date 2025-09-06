import pandas as pd

# Create a simple dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Dayo"],
    "Age": [25, 30, 35, 40],
    "Country": ["USA", "UK", "Canada", "Nigeria"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("people.csv", index=False)

# Load the CSV back
df_loaded = pd.read_csv("people.csv")

# Display basic info
print("DataFrame Loaded from CSV:")
print(df_loaded)

# Show summary statistics
print("\nSummary Statistics:")
print(df_loaded.describe(include="all"))
