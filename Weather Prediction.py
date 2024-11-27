weather=(1,1,1,0,1,1,0)
rainy=0
sunny=0
for day in weather:
    if day==1:
        rainy+=1
    else:
        sunny+=1
if rainy>sunny:
    print("It is likely to rain")
elif sunny>rainy:
    print("It is likely to not rain today")
else:
    print("The Chances to Rain and to not Rain are Equal")
