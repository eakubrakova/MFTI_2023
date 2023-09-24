prices = {'Adidas': 4298, 'Nike': 6550, 'Puma': 4490, 'Asics': 3879}
purchases = ["Adidas", "Nike"]

if len(purchases) == 0:
    print("Ваша корзина пуста")
elif len(purchases) == 1:
    total_cost = prices[purchases[0]]
    print("Стоимость заказа составила:", total_cost)
else:
    brand_counts = {}
    for purchase in purchases:
        if purchase in brand_counts:
            brand_counts[purchase] += 1
        else:
            brand_counts[purchase] = 1
    
    discount = 0
    total_cost = 0
    
    for brand, count in brand_counts.items():
        if count == 1:
            total_cost += prices[brand]
            discount += prices[brand] * 0.05
        else:
            total_cost += prices[brand] * count
            discount += prices[brand] * count * 0.1
    
    payment_without_discount = total_cost - discount
    print(f"Стоимость заказа составила: {total_cost}. С учетом скидки в {round(discount / total_cost * 100)}% — {payment_without_discount}")
