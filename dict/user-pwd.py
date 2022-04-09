user_pwd = {'Mary':'pass1', 'Jenny':'pass2', 'Mavis':'pass3',
            'Peter':'pass4', 'Alex':'pass5', 'Fanny':'pass6',
            'Davis':'pass7', 'Benny':'pass8', 'Daisy':'pass9',
            'John':'pass10'
}

username = input("Enter the username: ")
password = input("Enter the password: ")

#pwd = user_pwd.get(username,'Absent')

if username in user_pwd.keys():
    print('Username is found !!')
else:
    print('Username is not here !!')

if password in user_pwd.values():
    print('Password is found !!')
else:
    print('Password is not found !!')
