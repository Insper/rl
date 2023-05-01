DiscountedReturns = []
for t in range(len(Rewards)):
    G = 0.0
    for k,r in enumerate(Rewards[t:]):
        G += (y**k)*r
    DiscountedReturns.append(G)