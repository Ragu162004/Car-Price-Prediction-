import pandas as pd
import random

# Sample data for generating listings
car_names = [
    "Toyota Fortuner", "Hyundai Verna", "Maruti Suzuki Baleno", "Honda Civic", "Ford Endeavour",
    "Renault Captur", "Hyundai Creta", "Volkswagen Jetta", "Nissan X-Trail", "Mahindra Thar",
    "Maruti Suzuki Dzire", "Kia Seltos", "Toyota Corolla", "Hyundai Tucson", "Tata Nexon",
    "Jeep Compass", "Ford Figo Aspire", "Honda Jazz", "MG Hector", "Skoda Octavia", "Volkswagen Tiguan",
    "Tata Hexa", "Hyundai Venue", "Renault Triber", "Mahindra XUV300", "Toyota Yaris", "Kia Carnival"
]
companies = ["Toyota", "Hyundai", "Maruti", "Honda", "Ford", "Renault", "Volkswagen", "Nissan", "Mahindra", "Kia", "MG", "Skoda", "Tata", "Jeep"]
fuel_types = ["Petrol", "Diesel"]
years = range(2000, 2023)  # Car manufacturing years
prices = range(50000, 2500000, 5000)  # Prices between 50,000 to 2,500,000
kms_driven = range(1000, 150000, 1000)  # Kilometers driven between 1,000 to 150,000

# Generate 1000 random car listings
data = {
    "" : "",
    "name": [random.choice(car_names) for _ in range(1000)],
    "company": [random.choice(companies) for _ in range(1000)],
    "year": [random.choice(years) for _ in range(1000)],
    "Price": [random.choice(prices) for _ in range(1000)],
    "kms_driven": [random.choice(kms_driven) for _ in range(1000)],
    "fuel_type": [random.choice(fuel_types) for _ in range(1000)]
}

# Create DataFrame
car_data_df = pd.DataFrame(data)

# Save to CSV
file_path = 'car_listings.csv'
car_data_df.to_csv(file_path, index=False)

file_path
