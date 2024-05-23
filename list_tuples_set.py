l=['Bob', 'Rolf', 'Anne'] # list is mutable
t=('Bob', 'Rolf', 'Anne') # tuple is immutable
s={'Bob', 'Rolf', 'Anne'} # Can't repeat elements

print(l[0], t[0])

## Advanced Set Operations

Friends={"Bob", "Rolf","Anne"}
abroad={"Bob","Anne"}
local_friends=abroad.difference(Friends)
print(local_friends)
local_friends=Friends.difference(abroad)
print(local_friends)

print(Friends.union(abroad))

print(Friends.intersection(abroad))

print(Friends==abroad)
print(Friends is abroad)
