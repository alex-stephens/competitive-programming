# Competitive Programming 3
# Problem 489

while True:
    R = int(input())
    if R == -1: break

    print('Round ' + str(R))
    
    target = set(input())
    done, wrong = set(), 0
    guesses  = input()
    
    verdict, msg = None, ['You win.', 'You lose.', 'You chickened out.']
    
    for g in guesses:
        if g in done:
            continue
        else:
            done.add(g)
            
        if g in target: target.remove(g)
        else: wrong += 1
            
        if len(target) == 0: 
            verdict = 0
            break
        elif wrong == 7: 
            verdict = 1
            break
        
    if verdict == None: verdict = 2
    print(msg[verdict])
        
            
