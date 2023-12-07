def coin_change(coins, n, target):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if n <= 0:
        return 0
    return coin_change(coins, n-1, target) +\
        coin_change(coins, n, target-coins[n-1])

coins = [1, 2, 3]
n = len(coins)
target = 4
print(coin_change(coins, n, target))
