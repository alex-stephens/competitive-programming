# Competitive Programming 3
# Problem 10141

RFP = 1

while True:
    n, p = [int(x) for x in input().split()]
    if n == 0 and p == 0: break
    if RFP != 1: print('')
    
    reqs = []
    for _ in range(n):
        reqs.append(input())
        
    bestProposal, bestCompliance, bestPrice = None, 0, None 
    
    
    for _ in range(p):
        proposal = input()
        price, r = [float(x) for x in input().split()]
        
        # met requirements - no need to do anything with these
        for _ in range(int(r)): input()
        
        compliance = r / n
        
        if bestPrice == None:
            bestCompliance, bestProposal, bestPrice = compliance, proposal, price

        elif compliance > bestCompliance:
            bestCompliance, bestProposal, bestPrice = compliance, proposal, price
        
        elif compliance == bestCompliance and price < bestPrice:
            bestCompliance, bestProposal, bestPrice = compliance, proposal, price
            
            
            
            
    print('RFP #' + str(RFP))
    print(bestProposal)
    RFP += 1
