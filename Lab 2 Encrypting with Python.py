import csv

def load_dataset(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
    
dataset = load_dataset('SuperStore_data.csv')


total_orders = len(dataset)
print(f"Total orders: {total_orders}")


total_sales = sum(float(order['sales']) for order in dataset)
total_profit = sum(float(order['profit']) for order in dataset)
print(f"Total sales: ${total_sales}")
print(f"Total profit: ${total_profit}")


unique_customers = set()

unique_customers = unique_customers.add(order["customer"] for order in dataset)

unique_customer_number = len(unique_customers)
print("Unique customer names: ", unique_customers)
print("The total number of unique customers: ", unique_customer_number)


category_sales = {}

for order in dataset:
    category = order["category"]
    sales = float(order["sales"])
    category_sales[category] = category_sales.get(category, 0) + sales

print("Category Sales:")
for category, category_sales in category_sales.items():
    print(f"{category} : ${category_sales:.2f}")


class Product:
     
    def __init__(self, product_name, category, sales, profit):
          self.product_name = product_name
          self.category = category
          self.sales = float(sales)
          self.profit = float(profit)

    def calc_profit_margin(self):
        if self.sales == 0:
             return 0.0
        return (self.profit / self.sales) * 100


product_objs = {}
for order in dataset:
     product_name = order["product_name"]
     category = order["category"]
     sales = order["sales"]
     profit = order["profit"]

product_objs[product_name] = Product(product_name, category, sales, profit)

product_prof_margins = [
     (product.product_name, product.calc_profit_margin())
     for product in product_objs.values()
]


list_products = sorted(product_prof_margins, key=lambda x: x[1], reverse=True) [:5]

print("Top 5 Most Profitable Products:")
for i, (product_name, product_prof_margins) in enumerate(list_products, 1):
     print(f"{i}. {product_name} : {product_prof_margins:.2f}% profit margin")