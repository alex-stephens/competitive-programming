# Competitive Programming 3
# Problem 10026

T = int(input())

def val(char):
    if char in   ['A', 'J', 'S']: return 1
    elif char in ['B', 'K', 'T']: return 2
    elif char in ['C', 'L', 'U']: return 3
    elif char in ['D', 'M', 'V']: return 4
    elif char in ['E', 'N', 'W']: return 5
    elif char in ['F', 'O', 'X']: return 6
    elif char in ['G', 'P', 'Y']: return 7
    elif char in ['H', 'Q', 'Z']: return 8
    elif char in ['I', 'R']: return 9
    
def interlace(string1, string2):
    ans = ''
    for i in range(len(string2)):
        ans += string1[i] + string2[i]
    if len(string1) > len(string2):
        ans += string1[-1]
    return ans
    
vowel = ['A', 'U', 'E', 'O', 'I']
cons = ['J', 'S', 'B', 'K', 'T','C', 'L', 'D', 'M', 'V', 'N', 'W', \
        'F', 'X', 'G', 'P', 'Y', 'H', 'Q', 'Z', 'R']

for i in range(1,T+1):
    N = int(input())    
    print('Case ' + str(i) + ': ', end = '')

    
    vowelStr, consStr = '', ''
    maxV, maxC, numV, numC = 21, 5, (N+1)//2, N//2   
    V, C = 0, 0
    
    for i in range(numV // maxV):
        vowelStr += maxV * vowel[i]
        numV -= maxV
        V += 1
    for i in range(numC // maxC):
        consStr += maxC * cons[i]
        numC -= maxC
        C += 1
    
    if numV > 0: vowelStr += numV * vowel[V]
    if numC > 0: consStr  += numC * cons[C]
    
    vowelStr = ''.join(sorted(vowelStr))
    consStr = ''.join(sorted(consStr))
    
    print(interlace(vowelStr, consStr))