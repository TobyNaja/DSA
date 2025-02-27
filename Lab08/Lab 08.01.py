def convert_key(data):
    return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):
    coin_values = sorted(coins.keys(), reverse=True)
    result = {}
    total_coins = 0
    total_given = 0

    for coin in coin_values:
        if amount == 0:
            break
        result[coin] = 0
        for _ in range(coins[coin]):
            if amount >= coin or amount >= 0:
                amount -= coin
                total_given += coin
                total_coins += 1
                result[coin] += 1
            else:
                break

    if amount > 0:
        print("Coins are not enough.")
    else:
        print(f"Amount: {total_given}")
        print("Coin exchange result:")
        for coin in coin_values:
            print(f"  {coin} baht = {result.get(coin, 0)} coins")
        print(f"Number of coins: {total_coins}")

def main():
    import json
    amount = int(input())
    coins = convert_key(json.loads(input()))
    coinExchange(amount, coins)

main()
