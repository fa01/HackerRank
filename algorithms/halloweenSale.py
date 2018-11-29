
# You wish to buy video games from the famous online video game store Mist with s dollars.
# Usually, all games are sold at the same price, p dollars. 
# However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. 
# Specifically, the first game you buy during the sale will be sold at p dollars, but every subsequent game you buy will be 
# sold at exactly d dollars less than the cost of the previous one you bought. 
# This will continue until the cost becomes less than or equal to m dollars, after which every game you buy will cost m dollars each.
# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if(p == s):
        return 1
    elif(p > s):
        return 0
    else:
        count = 1
        remaining = s - p
        cost = p - d
        if(remaining < cost):
            return 1
        while(remaining > 0 and cost > m and remaining > cost):
            count += 1
            remaining = remaining - cost
            cost = cost - d
        while(remaining >= m):
            count += 1
            remaining = remaining - m
        return count
