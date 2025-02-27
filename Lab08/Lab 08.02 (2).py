class Item:
    def __init__(self, name, price: int, weight: float):
        self.__name = name
        self.__price = price
        self.__weight = weight
        
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_weight(self):
        return self.__weight
    
def knapsack(amount, itemList):

    value_per_weight = []
    for item in itemList:
        value_per_weight.append((item, item.get_price() / item.get_weight()))
    
    value_per_weight.sort(key=lambda x: x[1], reverse=True)
    
    total_value = 0
    total_weight = 0
    items_in_bag = []

    for item, value in value_per_weight:
        if total_weight + item.get_weight() <= amount:
            total_value += item.get_price()
            total_weight += item.get_weight()
            items_in_bag.append(item)
    

    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    for item in items_in_bag:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
    print(f"Total: {total_value} THB")
    
def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_it = json.loads(input())
        items.append(Item(item_it['name'], item_it['price'], item_it['weight']))
        num_items = num_items - 1
    knapsack_capasity = float(input())
    knapsack(knapsack_capasity, items)

main()
