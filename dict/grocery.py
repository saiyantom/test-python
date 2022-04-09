item_price = {'TV':2350,'Notebook':5250,'Table':3045}
item_quantity = {'TV':10,'Notebook':26,'Table':73}

total=0

for grocery in item_price.keys():
    for product in item_quantity.keys():
        if grocery == product:
            total += item_quantity[product] * item_price[grocery]

print(f'Total bill: {total}')
