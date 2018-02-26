# Competitive Programming 3
# Problem 579

while True:
    hrs, mins = [int(x) for x in input().split(':')]
    if hrs == 0 and mins == 0: break

    # hour includes contribution from minutes
    minAngle = mins * 360/6
    hrAngle = (hrs % 12) * 360/12 + minAngle/12 
    
    angle = abs(hrAngle - minAngle)
    angle = min(angle, 360 - angle) # value between 0 and 180
    print("{:.3f}".format(angle))

