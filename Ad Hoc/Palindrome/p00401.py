# Competitive Programming 3
# Problem 00401

def isPalindrome(string):
    return True if string == string[::-1] else False

org = {'A':'A', 'E':'3', 'H':'H', 'I':'I', 'J':'L', 'L':'J', \
       'M':'M', 'O':'O', 'S':'2', 'T':'T', 'U':'U', 'V':'V', \
       'W':'W', 'X':'X', 'Y':'Y', 'Z':'5', '1':'1', '2':'S', \
       '3':'E', '5':'Z', '8':'8'}

def isMirror(string):
    result, length = '', len(string)
    for i in range(length-1,-1,-1):
        if string[i] in org:
            result += org[string[i]]
        else:
            return False

    if result == string: return True
    else: return False
        
while True:
    try:
        string = input()
    except EOFError:
        break
        
    msg = [' -- is not a palindrome.', ' -- is a regular palindrome.', \
           ' -- is a mirrored string.', ' -- is a mirrored palindrome.']
    
    pal, mir = isPalindrome(string), isMirror(string)
    if pal and mir: i = 3
    elif mir: i = 2
    elif pal: i = 1
    else: i = 0  
    
    print(string + msg[i] + '\n')
        