import pandas as pd
import os

try:
    # 🔍 Load the messy CSV file
    df = pd.read_csv("sample_dirty.csv", on_bad_lines="skip")

    # 🧠 Trim whitespace from column headers
    df.columns = [col.strip() for col in df.columns]

    # 🧼 Remove rows that are fully empty
    df.dropna(how="all", inplace=True)

    # 🪄 Strip whitespace from string cells - safer method
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    # 💰 Price cleanup with safety check
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df[df['price'] > 0]
        print(f"💸 Non-null prices: {df['price'].notna().sum()}")
    else:
        print("⚠️ 'price' column not found. Skipping price cleanup.")

    # 📁 Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # 💾 Save the cleaned data
    df.to_csv("output/cleaned_output.csv", index=False)

    print("✅ CSV cleaned and saved as 'output/cleaned_output.csv'")

except Exception as e:
    print(f"⚠️ Oops! Something went wrong: {e}")






