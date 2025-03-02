import pandas as pd

# Load the CSV file
df = pd.read_csv("marketing_campaign_data.csv")

# Convert 'created_at' column to datetime format (if not already)
df['created_at'] = pd.to_datetime(df['created_at'])

# Aggregate total units sold per product
product_sales = df.groupby("product_id")["quantity"].sum().reset_index()

# Define ad performance classification
def classify_performance(units):
    if units >= 30:
        return "Outstanding"
    elif 20 <= units <= 29:
        return "Satisfactory"
    elif 10 <= units <= 19:
        return "Unsatisfactory"
    elif 1 <= units <= 9:
        return "Poor"
    else:
        return "No Sales"

# Apply classification function
product_sales["ad_performance"] = product_sales["quantity"].apply(classify_performance)

# Sort by total units sold in descending order
product_sales = product_sales.sort_values(by="quantity", ascending=False)

# Display the result
print(product_sales)
