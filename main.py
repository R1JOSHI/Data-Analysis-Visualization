# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using file path as local path
file_path = 'Enter the path where csv file is saved in your local machine'
df = pd.read_csv(file_path)

# Convert date columns to datetime format
df['booking_date'] = pd.to_datetime(df['booking_date'])
df['travel_date'] = pd.to_datetime(df['travel_date'], dayfirst=True)

# Observation 1: Booking trends over time
booking_trends = df['booking_date'].dt.to_period('M').value_counts().sort_index()

# Observation 2: Distribution of selling prices
selling_price_distribution = df['selling_price']

# Observation 3: Popular routes (from_airport to to_airport)
popular_routes = df.groupby(['from_airport', 'to_airport']).size().sort_values(ascending=False).head(10)

# Observation 4: Refund Analysis
refund_counts = df['refund_status'].value_counts(normalize=True) * 100
total_refund_amount = df['refund_amount'].sum()

# Observation 5: Payment Method Preferences
payment_method_distribution = df.groupby('payment_method')['selling_price'].agg(['count', 'mean']).sort_values(by='count', ascending=False)

# Plotting the Visualization 

# Booking trends over time
plt.figure(figsize=(10, 6))
booking_trends.plot(kind='bar', color='skyblue')
plt.title('Booking Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Distribution of selling prices
plt.figure(figsize=(10, 6))
sns.histplot(selling_price_distribution, kde=True, color='green')
plt.title('Distribution of Selling Prices')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()

# Popular routes
plt.figure(figsize=(10, 6))
popular_routes.plot(kind='bar', color='orange')
plt.title('Top 10 Popular Routes')
plt.xlabel('Route (From -> To)')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Refund status distribution
plt.figure(figsize=(8, 5))
refund_counts.plot(kind='bar', color='purple')
plt.title('Refund Status Distribution')
plt.xlabel('Refund Status')
plt.ylabel('Percentage of Total Bookings')
plt.xticks(rotation=0)
plt.show()

# Payment method distribution
plt.figure(figsize=(10, 6))
payment_method_distribution['count'].plot(kind='bar', color='blue')
plt.title('Payment Method Preferences')
plt.xlabel('Payment Method')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Summary of Observations
summary = {
    "Booking Trends": booking_trends,
    "Selling Price Distribution": selling_price_distribution.describe(),
    "Popular Routes": popular_routes,
    "Refund Status Distribution": refund_counts,
    "Total Refund Amount": total_refund_amount,
    "Payment Method Distribution": payment_method_distribution
}

summary
