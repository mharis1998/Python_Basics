## Lists of tuples
users=[
    (0,'Bob','password'),
    (1,'Rolf','longp4assowrd')
]

username_mapping={user[1]: user for user in users}

username_input=input("Please enter your user name: ")
password_input=input("PLease enter your password: ")

#print(username_mapping["Bob"])

_,username,password=username_mapping[username_input]

if password==password_input:
    print("Your detail is correct")
else:
    print("Your detail are incorrect")
    