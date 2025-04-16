inventory = [
    {"product_id": 1, "name": "Laptop", "price": 50000, "stock": 10},
    {"product_id": 2, "name": "Mobile", "price": 15000, "stock": 20},
    {"product_id": 3, "name": "Headphones", "price": 2000, "stock": 50},
]

cart = []
orders = []
order_details = []
customers = []
payments = []

customer_id = input("Customer ID: ")
customer_name = input("Customer Name: ")
customer_address = input("Shipping Address: ")
customers.append({"customer_id": customer_id, "name": customer_name, "address": customer_address})

for product in inventory:
    print(f"ID: {product['product_id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")

while True:
    product_id = int(input("Product ID to add to cart (0 to stop): "))
    if product_id == 0:
        break
    quantity = int(input("Quantity: "))
    for product in inventory:
        if product["product_id"] == product_id:
            if product["stock"] >= quantity:
                cart.append({"product_id": product_id, "name": product["name"], "quantity": quantity, "price": product["price"]})
                product["stock"] -= quantity
            break

for item in cart:
    print(f"Product: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Total: {item['quantity'] * item['price']}")

confirm = input("Place the order? (yes/no): ").lower()
if confirm == "yes":
    order_id = len(orders) + 1
    total_amount = sum(item['quantity'] * item['price'] for item in cart)
    orders.append({"order_id": order_id, "customer_id": customer_id, "total_amount": total_amount})
    for item in cart:
        order_details.append({"order_id": order_id, "product_id": item["product_id"], "quantity": item["quantity"], "price": item["price"]})
    payment_mode = input("Payment Mode (Card/Cash/UPI): ")
    payments.append({"order_id": order_id, "amount": total_amount, "payment_mode": payment_mode})
    print("Order placed successfully!")
    print(f"Shipping to {customer_name} at {customer_address}.")
else:
    print("Order canceled.")

for order in orders:
    print(f"Order ID: {order['order_id']}, Customer ID: {order['customer_id']}, Total: {order['total_amount']}")

for product in inventory:
    print(f"ID: {product['product_id']}, Name: {product['name']}, Stock: {product['stock']}")