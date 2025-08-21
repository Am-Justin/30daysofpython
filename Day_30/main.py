print("Day 30: End of the road, start of your journey.")
h = 16
espace = h - 1
a = 1
for i in range(h):
    print(" "*espace + "*"*a)
    espace-=1
    a+=2
for i in range(8):
    print(" "*14+"*"*4)    
     
print("It was a real pleasure to participate in this challenge,\n during which I had the opportunity \nto review the basics of Python.")