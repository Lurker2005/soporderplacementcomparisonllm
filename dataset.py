import csv
import random

shop_names = [f"Shop_{i+1}" for i in range(100)]
item_names = [f"Item_{j+1}" for j in range(100)]

with open('shops_dataset.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Shop Name", "Product ID", "Item Name", "Price", "Shipping Cost", "Delivery Time",
                     "Return Policy", "Stock Status", "Avg. Rating", "Promotions", "Loyalty Program",
                     "Customer Support", "Countries Served"])
    for shop in shop_names:
        for item_id, item in enumerate(item_names, start=1):
            writer.writerow([
                shop,
                f"{shop}_P{item_id:04}",
                item,
                random.randint(500, 50000),
                random.randint(20, 700),
                f"{random.randint(1,7)} days",
                f"{random.choice(['7 days', '14 days', '30 days'])}",
                random.choice(['In Stock', 'Out of Stock']),
                round(random.uniform(3.0, 5.0), 1),
                random.choice(['None', '10% off', 'Free shipping']),
                random.choice(['Yes', 'No']),
                f"{round(random.uniform(3.0, 5.0), 1)}/5",
                "India"
            ])
