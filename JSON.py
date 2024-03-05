import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(url)
data = response.json()

products = data.get("products", {})

product_list = []
for key, value in products.items():
    product_list.append({
        "title": value["title"],
        "price": float(value["price"]),  
        "popularity": int(value["popularity"])  
    })

sorted_data = sorted(product_list, key=lambda x: x['popularity'], reverse=True)

print("Title\t\tPrice")
print("-" * 20)
for product in sorted_data:
    print(f"{product['title']}\t${product['price']}")