
def maxprofit(p, n):
    # if n<=0:return 0

    # ans = 0
    # for i in range(n):
    #     cut = i+1
    #     cans = prices[i]+maxprofit(p, n-cut)
    #     ans = max(ans, cans)
    # return ans

    dp = [0]

    for j in range(1,n+1):
        ans = 0
        for i in range(j):
            cut = i+1
            cans = p[i]+dp[j-cut]
            ans = max(ans, cans)
        dp.append(ans)
    return dp[-1]

prices = [1,5,8,9,10,17,17,20]
print(maxprofit(prices,len(prices)))