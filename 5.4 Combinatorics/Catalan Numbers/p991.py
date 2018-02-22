# Competitive Programming 3
# Problem 991


catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]

while True:
    try: 
        N = int(input())
    except EOFError:
        break
    
    print(catalan[N])
        