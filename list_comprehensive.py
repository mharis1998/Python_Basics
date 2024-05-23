friends=['Rolf','Sam','Samantha','Saurabh','Jen']
start_s=[]
for f in friends:
    if f.startswith('S'):
        start_s.append(f)
print(start_s)

start_j=[f for f in friends if f.startswith('J')]

print(start_j)
print(friends is start_j)
print("friends: ", id(friends), "start_s: ", id(start_s))

head, *tail=[1,2,3,4,5]
print(tail)
print(head)
