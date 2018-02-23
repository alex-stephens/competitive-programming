# Competitive Programming 3
# Problem 146

'''
Function to compute next lexicographic permutation of a string
'''
def nextLex(A):
    length = len(A)
    found = False
    for k in range(length-2, -1, -1):
        if A[k] < A[k+1]:
            found = True
            break
    
    if not found: return A[::-1]
    
    for l in range(length-1, k, -1):
        if A[l] > A[k]: break
    
    B = list(A)
    B[l], B[k] = B[k], B[l]
    B[k+1:] = B[k+1:][::-1]
    
    return ''.join(B)


while True:
    string = input()
    if string == '#':
        break
    new = nextLex(string)
    
    if new[0] < string[0] or new == string: # rolled over or identical
        print("No Successor")
    else:
        print(new)
    
    
    
    
    
    
    
    