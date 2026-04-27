import pandas as pd

# Read the SLMAG.XYZ file
# The file appears to be space-separated with column names in the first line
# There's a separator line after headers, but pandas can handle it
# Note: This file is large (~50MB), so reading may take some time
# Skip the separator line (line 1, 0-indexed) which starts with / and contains =

df = pd.read_csv('/Users/sgkang09/Project/reditt_iron_magnetic/data/SLMAG.XYZ', sep='\s+', header=0, skiprows=[1])

# Display the first few rows to verify
print(df.head())

# Print some info about the dataframe
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Optional: Save to a more efficient format if needed
# df.to_parquet('data.parquet')  # Uncomment to save as Parquet

# Optional: Save to a more efficient format if needed
# df.to_parquet('data.parquet')  # Uncomment to save as Parquet