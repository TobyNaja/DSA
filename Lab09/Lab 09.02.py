import json

def knapsackV2(amount, itemList):
    if isinstance(itemList, str):
        itemList = json.loads(itemList)
    
    n = len(itemList)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    selected = [[[] for _ in range(amount + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = itemList[i-1][0]
        item_price = itemList[i-1][1]
        item_weight = itemList[i-1][2]
        
        for w in range(amount + 1):
            if item_weight > w:
                dp[i][w] = dp[i-1][w]
                selected[i][w] = selected[i-1][w]
            else:
                if dp[i-1][w] > dp[i-1][w-item_weight] + item_price:
                    dp[i][w] = dp[i-1][w]
                    selected[i][w] = selected[i-1][w]
                else:
                    dp[i][w] = dp[i-1][w-item_weight] + item_price
                    selected[i][w] = selected[i-1][w-item_weight] + [i-1]
    
    selected_items = selected[n][amount]
    total_price = dp[n][amount]
    
    result = []
    for idx in selected_items:
        result.append([itemList[idx][0], itemList[idx][2], itemList[idx][1]])
    
    result.sort()
    
    print(f"Total: {total_price}")
    for name, weight, price in result:
        print(f"{name} -> {weight} kg -> {price} THB")

def main():
    itemList = input()
    amount = int(input())
    knapsackV2(amount, itemList)

main()