# Competitive Programming 3
# Problem 1061

def valid(p1, p2, child):
    if (child[0] in p1 and child[1] in p2) or \
        (child[1] in p1 and child[0] in p2):
        return True
    return False

t = 1
while True:
    p1, p2, child = input().split()
    if (p1, p2, child) == ('E', 'N', 'D'): break
    
    combs = [ 'OO',  'AB', 'BB', 'BO', 'AA','AO' ]
    options = {'A':['AA','AO'], 'B':['BB','BO'], 'AB':['AB'], 'O':['OO']}
    ABO = {'AA':'A', 'AB':'AB', 'AO':'A', 'BO':'B', 'BB':'B', 'OO':'O'}
    
    typ, rh, ans = [], [], []
    
    p1options = options[p1[:-1]] if p1 != '?' else options[p2[:-1]] # never unknown
    if (p1 == '?' or p2 == '?'): p2options = combs
    else: p2options = options[p2[:-1]]
    childoptions = options[child[:-1]] if child != '?' else combs 
    childUnknown = True if child == '?' else False
    
    for x in p1options:
        for y in p2options:
            for z in childoptions:
                if valid(x, y, z): 
                    if childUnknown: typ.append(z)
                    else: typ.append(y)
                    
    if childUnknown:
        rh.append('-')
        if '+' in p1 or '+' in p2: rh.append('+')
                    
    else: 
        if not ('+' in child and '+' not in p1 and '+' not in p2): rh.append('-')
        rh.append('+')
        
    for x in typ: 
        for r in rh:
            if (ABO[x] + r not in ans): ans.append(ABO[x] + r)
            

    print("Case {}: ".format(t), end='')
    if child == '?':
        print(*[p1, p2], end=' ')
        if ans == []: print('IMPOSSIBLE ', end='')
        else: 
            print('{', end='')
            print(*ans, sep=', ', end='')
            print('}')
    
    elif p1 == '?':
        if ans == []: print('IMPOSSIBLE ', end='')
        else: 
            print('{', end='')
            print(*ans, sep=', ', end='')
            print('} ', end='')
        print(*[p2, child])

    elif p2 == '?':
        print(p1, end=' ')
        if ans == []: print('IMPOSSIBLE ', end='')
        else: 
            print('{', end='')
            print(*ans, sep=', ', end='')
            print('} ', end='')
        print(child)
        
    t += 1
