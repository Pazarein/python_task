def total_revenue(purchases):
    return sum(item['price'] * item['quantity'] for item in purchases)

def items_by_category(purchases):
    categories = {}
    for item in purchases:
        category = item['category']
        if category not in categories:
            categories[category] = []
        if item['item'] not in categories[category]:
            categories[category].append(item['item'])
    return categories

def expensive_purchases(purchases, min_price):
    return [item for item in purchases if item['price'] >= min_price]

def average_price_by_category(purchases):
    categories = {}
    for item in purchases:
        category = item['category']
        if category not in categories:
            categories[category] = {'total_price': 0, 'count': 0}
        categories[category]['total_price'] += item['price']
        categories[category]['count'] += 1
    return {category: data['total_price'] / data['count'] for category, data in categories.items()}

def most_frequent_category(purchases):
    category_quantities = {}
    for item in purchases:
        category = item['category']
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += item['quantity']
    return max(category_quantities, key=category_quantities.get)

# Исходные данные
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Выполнение анализа
revenue = total_revenue(purchases)
items_by_cat = items_by_category(purchases)
expensive_items = expensive_purchases(purchases, 1.0)
avg_price_by_cat = average_price_by_category(purchases)
most_freq_cat = most_frequent_category(purchases)

# Вывод отчета
print(f"Общая выручка: {revenue}")
print(f"Товары по категориям: {items_by_cat}")
print(f"Покупки дороже 1.0: {expensive_items}")
print(f"Средняя цена по категориям: {avg_price_by_cat}")
print(f"Категория с наибольшим количеством проданных товаров: {most_freq_cat}")