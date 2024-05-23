## 

add=lambda x,y: x+y
print(add(2,3))

sequence=[1,2,3,4,5]
doubled=[(lambda x: x*2)(x) for x in sequence]
print(doubled)
doubled=list(map(lambda x: x*2, sequence))
print(doubled)