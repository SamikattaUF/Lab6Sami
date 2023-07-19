def main():
    menu = True
    # Repeat menu until menu becomes false
    # Set menu to false when option_menu is 3
    while menu == True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        option_menu = input('Please enter an option: ')
        # Results of option menu inputs
        if option_menu == '1':
            password = input('Please enter your password to encode: ')
            password_encoded = encode(password)
            print(password_encoded)
            print('Your password has been encoded and stored!')
        elif option_menu == '2':
            password_decoded = str(decode(password_encoded))
            print('The encoded password is', password_encoded+', and the original password is', password_decoded)
        elif option_menu == '3':
            menu = False

def encode(password):
    # Take password and increase each digit by 3
    encoded = ''
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded

def decode(password_encoded):
    # Take decoded password and decrease each digit by 3
    pass

if __name__ == '__main__':
    main()

def decode(password_encoded):
    # Take encoded password and decrease each digit by 3
    decoded = ''
    for i in range(len(password_encoded)):
        decoded += str((int(password_encoded[i]) - 3) % 10)
    return decoded
