access = input(' Type [A]ccess [E]xit: ')

if access == 'E':
    print('Exiting the system')
elif access != 'A':
    print('Invalid option')
else:
    password = input('Enter the password: ')
    password_allowed = '1234'

    if access == 'A' and password == password_allowed :
        print('Access granted')
    else:
        print('Access denied')