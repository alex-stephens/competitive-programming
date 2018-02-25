# Competitive Programming 3
# Problem 454

T = int(input())
input()

for t in range(T):
    words = []
    while True:
        if t < T-1:
            line = input()
            words.append(line)
            if line == '': break
        else:
            try: 
                line = input()
                words.append(line)
            except EOFError: break
    
    if t > 0: print('')
    words.sort()
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            s1, s2 = words[i].replace(' ',''), words[j].replace(' ','')
            if sorted(s1) == sorted(s2):
                print(words[i], '=', words[j])