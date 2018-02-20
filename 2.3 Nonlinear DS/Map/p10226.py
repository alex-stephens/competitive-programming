# Competitive Programming 3
# Problem 10226

T = int(input())
input()

for t in range(T):
    counts, num = {}, 0
    while True:
        try:
            tree = input()
        except EOFError:
            break
        if tree == '': break
        
        num += 1
        if tree in counts:
            counts[tree] += 1
        else:
            counts[tree] = 1
        
    if t > 0: print('')
    for key, val in sorted(counts.items()):
        print("{} {:.4f}".format(key, 100*val/num))
    t += 1
        
    
    