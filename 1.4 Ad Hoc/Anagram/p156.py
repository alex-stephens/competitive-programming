# Competitive Programming 3
# Problem 156

words, words_orig = [], []

while True: 
    line = input()
    if line == '#': break
    words_orig += line.split()
    words += [list(x) for x in line.split()]
    
words.sort()
words_orig.sort()

for i in range(len(words)): words[i] = list(''.join(words[i]).lower())
for i in range(len(words)): words[i].sort()


for i in range(len(words)): 
    if words.count(words[i]) == 1: print(words_orig[i])
