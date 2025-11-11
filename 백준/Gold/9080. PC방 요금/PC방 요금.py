import math

t = int(input())

for _ in range(t):
    line = input().split()
    timepart = line[0].split(':')
    starthh = int(timepart[0])
    startmm = int(timepart[1])
    d = int(line[1])
    cost1 = math.ceil(d / 60) * 1000
    cost2 = 0
    currenttime = starthh * 60 + startmm
    remainingd = d
    normalminutes = 0
    dayminutes = 1440
    nightstart = 22 * 60
    nightend = 8 * 60

    while remainingd > 0:
        timeofday = currenttime % dayminutes
        
        isnight = (timeofday >= nightstart) or (timeofday < nightend)
        
        if isnight:
            if normalminutes > 0:
                cost2 += math.ceil(normalminutes / 60) * 1000
                normalminutes = 0
            
            cost2 += 5000
            
            nightminutes = 0
            if timeofday < nightend:
                nightminutes = nightend - timeofday
            else:
                nightminutes = (dayminutes - timeofday) + nightend
                
            usedminutes = min(remainingd, nightminutes)
            remainingd -= usedminutes
            currenttime += usedminutes
            
        else:
            normalblockminutes = nightstart - timeofday
            usedminutes = min(remainingd, normalblockminutes)
            
            remainingd -= usedminutes
            currenttime += usedminutes
            normalminutes += usedminutes
            
    if normalminutes > 0:
        cost2 += math.ceil(normalminutes / 60) * 1000
        
    print(min(cost1, cost2))