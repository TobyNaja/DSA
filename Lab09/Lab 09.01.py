import json

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, coins):
    print(f"Amount: {amount}")
    types = sorted(coins, reverse=True)
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_usage = [{coin: 0 for coin in types} for _ in range(amount + 1)]
    
    for i in range(1, amount + 1):
        for coin in types:
            if coin <= i and coin_usage[i - coin][coin] < coins[coin]:
                temp_usage = coin_usage[i - coin].copy()
                temp_usage[coin] += 1
                if dp[i - coin] + 1 < dp[i]:
                    dp[i], coin_usage[i] = dp[i - coin] + 1, temp_usage
    
    if dp[amount] == float('inf'):
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total = sum(coin_usage[amount].values())
        for coin in types:
            print(f"  {coin} baht = {coin_usage[amount][coin]} coins")
        print(f"Number of coins: {total}")

def main():
    amount = int(input().strip())
    coins = convert_key(json.loads(input().strip()))
    coin_exchange(amount, coins)

main()