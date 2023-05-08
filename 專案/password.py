print('Please enter password.')
password=input()
password=password.replace(' ','')
if password == 'Raymond-Tai11':
    print('Welcome!')

else:
    while password!= 'Raymond-Tai11':
        print('Please enter password again.')
        password=input()
        password=password.replace(' ','')
        if password== 'Raymond-Tai11':
            print('Welcome!')
            break

