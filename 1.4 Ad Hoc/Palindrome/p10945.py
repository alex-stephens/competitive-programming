# Competitive Programming 3
# Problem 10945

while True:
    string = input()
    if string == "DONE": break
    string = string.lower()

    newstring = ''.join([string[i] for i in range(len(string)) \
                         if string[i] not in ' !?.,'])
    
    if newstring == newstring[::-1]:
        print("You won't be eaten!")
    else:
        print("Uh oh..")