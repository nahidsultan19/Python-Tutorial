usernames = []
passwords = []


def main():
    register()


def register():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    usernames.append(username)
    passwords.append(password)

    answer = input('Do you want to make another registrations?')
    if answer == 'y':
        register()
    else:
        registration()


def registration():
    print(f'List of usernames: {usernames}')
    print(f'List of passwords: {passwords}')


main()
