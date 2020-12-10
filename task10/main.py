numbers = sorted(list(map(int, open("data", "r").read().split('\n'))))

dp = [0] * 100
dp[0] = 1

numbers.insert(0, 0)
numbers.append(149)

for (i, n) in zip(range(0, 1000), numbers):
    if i == 0: 
        continue
    
    for shift in range(1, 4):
        previndex = i - shift
        if previndex < 0:
            break

        prev = numbers[previndex]
        if n - prev > 3:
            break
        
        dp[i] += dp[i-shift]

print(dp[-5])
        


