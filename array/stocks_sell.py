def find_lmax_lmin(price):
    #lmin = []
    #lmax = []

    """
    if price[0] > price[1]:
        lmax.append((0, price[0]))
    else:
        lmin.append((0, price[0]))
    """
    
    while index < len(price)-1:
        curr = price[index]
        nxt = price[index+1]


        if prev < curr > nxt:
            lmax = curr
        elif prev > curr < nxt:
            lmin = curr

        index = index + 1

    if price[-1] > price[-2]:
        lmax.append((len(price)-1, price[-1]))
    else:
        lmin.append((len(price)-1, price[-1]))
    print lmax, lmin
    return lmax, lmin

def calc_profit(price, lmin, lmax):
    profit = 0
    for buy_day in lmin:
        print "Buy on day: %s at: %s"%(buy_day[0], buy_day[1])
        for sell_day in lmax:
            if sell_day[0] < buy_day[0]:
                continue
            print "Sell on day: %s at: %s"%(sell_day[0], sell_day[1])
            profit = profit + sell_day[1] - buy_day[1]
            lmax.remove(sell_day)

    print "Max Profit: %s"%profit

price = [100, 180, 260, 310, 40, 535, 695]

lmax, lmin = find_lmax_lmin(price)
#calc_profit(price, lmin, lmax)
