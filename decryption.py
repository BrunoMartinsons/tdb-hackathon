# Encryption of message
def encryption():
    user_input = input(str("Write your message: "))
    encrypted = 0
    print()
    print("What kind of encryption do you want?")
    print()
    operator = input("1. Letter number\n2. Caesar cipher w/ numbers & symbols\n")
    print()
    operator = str(operator)
    if operator == "1":  # Continues in "Letter_number" because user chose letter number
        letter_number(user_input)

    elif operator == "2":  # Continues in "Caesar_cipher" because user chose caesar cipher
        caesar_cipher(user_input)

    else:
        print("The input was wrong!")

    print(encrypted)


# Decryption method
def decryption():
    user_choose = (input("What kind of encryption is the message? Is it:\n1. Letter number\n2. Caesar cipher\n"))
    print()

    # Letter number decryption
    if user_choose == "1":
        decrypted = (input("Write the numbers and remember to have spaces between each pair!: "))
        decrypted_split = decrypted.split()
        for num in decrypted_split:
            print(chr(int(num)), end=" ")

    # Caesar encryption
    elif user_choose == "2":
        user_input = input(str("Enter the message you want decrypted: "))
        decrypted_msg = ' '
        for letter in user_input:
            decrypted_msg += chr(ord(letter) - 5)
        print("Your decrypted message is:" + decrypted_msg)


# Encryption using Letter Number
def letter_number(input_user):
    for letter in input_user:
        print(ord(letter), end=" ")


# Encryption using Caesar cipher
def caesar_cipher(input_user):
    encrypted_msg = ''
    for letter in input_user:
        encrypted_msg += chr(ord(letter) + 5)
    print(encrypted_msg)


# Start of code
encrypt_or_decrypt = input("Do you want to encrypt or decrypt?: ").upper()
print()

# Moves to "ENCRYPTION" method in line 2
if encrypt_or_decrypt == "ENCRYPT":
    encryption()

# Moves to "DECRYPTION" method in line 24
elif encrypt_or_decrypt == "DECRYPT":
    decryption()

else:
    print("User input not correct")



