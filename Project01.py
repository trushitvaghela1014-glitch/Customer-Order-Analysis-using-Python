# Create a list of customer names
customer_names = ["Alice", "Bob", "Charlie", "Diana"]   
# Store each customer's order details (customer name, product, price, category) as 
# tuples inside a list
orders = [
    ("Alice", "Laptop", 1200, "Electronics"),
    ("Bob", "Book", 20, "Education"),
    ("Charlie", "Headphones", 150, "Electronics"),
    ("Diana", "Desk", 300, "Furniture")
]
#Use a dictionary where keys are customer names and values are lists of ordered products to store the orders for each customer
customer_orders = {}
for customer_name in customer_names:
    customer_orders[customer_name] = []

for order in orders:
    customer_name, product, price, category = order
    customer_orders[customer_name].append((product, price, category))

### 2. Classify products by category
# Use a dictionary to map each product to its respective category
product_categories = {}
for order in orders:
    product, category = order[1], order[3]
    product_categories[product] = category

  #• Create a set of unique product categories 
unique_categories = set(product_categories.values())  

#• Display all available product categories 
print("Available product categories:")
for category in unique_categories:
    print(f"- {category}")

    #3. Analyze customer orders 
#• Use a loop to calculate the total amount each customer spends 
customer_spending = {}
for order in orders:
    customer_name, product, price, category = order
    if customer_name in customer_spending:
        customer_spending[customer_name] += price
    else:
        customer_spending[customer_name] = price

        #• If the total purchase value is above $100, classify the customer as a high-value buyer 
high_value_buyers = [] 
for customer_name, total_spent in customer_spending.items():
    if total_spent > 100:
        high_value_buyers.append(customer_name)

        #• If it is between $50 and $100, classify the customer as a moderate buyer 
moderate_buyers = []
for customer_name, total_spent in customer_spending.items():
    if 50 < total_spent <= 100:
        moderate_buyers.append(customer_name)
        print(f"{customer_name} is a moderate buyer with total spending of ${total_spent}")

        #• If it is below $50, classify them as a low-value buyer 
low_value_buyers = []
for customer_name, total_spent in customer_spending.items():
    if total_spent <= 50:
        low_value_buyers.append(customer_name)

    #4. Generate business insights 

       #• Calculate the total revenue per product category and store it in a dictionary 
revenue_per_category = {}
for order in orders:
    product, price, category = order[1], order[2], order[3]
    if category in revenue_per_category:
        revenue_per_category[category] += price
    else:
        revenue_per_category[category] = price 
        print("Total Revenue per product category:") 
for category, revenue in revenue_per_category.items():
    print(f"- {category}: ${revenue}")

    #• Extract unique products from all orders using a set 
unique_products = set(product_categories.keys())
print("Unique products ordered:")
for product in unique_products:
    print(f"- {product}")

      #• Use a list comprehension to find all customers who purchased electronics 
electronics_buyers = [customer_name for customer_name, orders in customer_orders.items() for product, price, category in orders if category == "Electronics"]
print("Customers who purchased electronics:")
for buyer in electronics_buyers:
    print(f"- {buyer}")

    #• Identify the top three highest-spending customers using sorting 
sorted_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
top_three_customers = sorted_customers[:3]
print("Top three highest-spending customers:")
for customer_name, total_spent in top_three_customers:
    print(f"- {customer_name}: ${total_spent}")

    #5. Organize and display data 
    #• Print a summary of each customer’s total spending and their classification 
print("Customer Summary:")
for customer_name in customer_names:
    total_spent = customer_spending.get(customer_name, 0)
    if customer_name in high_value_buyers:
        classification = "High-value buyer"
    elif customer_name in moderate_buyers:
        classification = "Moderate buyer"
    else:
        classification = "Low-value buyer"
    print(f"- {customer_name}: Total Spending = ${total_spent}, Classification = {  classification}") 

    #• Use set operations to find customers who purchased from multiple categories 
categories_per_customer = {}
for customer_name, orders in customer_orders.items():  
    categories = set(category for product, price, category in orders)
    categories_per_customer[customer_name] = categories    
multi_category_buyers = [customer_name for customer_name, categories in categories_per_customer.items() if len(categories) > 1]
print("Customers who purchased from multiple categories:")
for buyer in multi_category_buyers:
    print(f"- {buyer}")

    # Identify customers who bought both Electronics and Clothing

electronics_and_clothing_buyers = [
    customer_name
    for customer_name, categories in categories_per_customer.items()
    if "Electronics" in categories and "Clothing" in categories
]

print("Customers who bought both Electronics and Clothing:")

for buyer in electronics_and_clothing_buyers:
    print(f"- {buyer}")



        