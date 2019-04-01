# Caesar Cipher to encrypt messages (only encrypts upper and lower case letters), symbols and spaces are not changed.


def main():
    user_choice = input("Would you like to (encrypt) or (decrypt?) a sentence?")
    if user_choice.lower() == "encrypt":
        shift = int(input("How many shifts do you want? "))
        sentence = input("What sentence do you want to encrypt? ")
        encrypted_sentence = encrypt(sentence, shift)
        print(encrypted_sentence)
        input("\nPress enter to close the program")
    elif user_choice.lower() == "decrypt":
        shift = int(input("How many shifts is the encrypted message? "))
        sentence = input("What sentence do you want to decrypt? ")
        decrypted_sentence = decrypt(sentence, shift)
        print(decrypted_sentence)
        input("\nPress enter to close the program")
        

def encrypt(sentence, shift):
    """Encrypts the sentence using the shift"""
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha() == False:  # If char is not a letter
            encrypted_sentence += char
        elif char.isupper() == True and (ord(char) + shift) > ord("Z"):
            total_number = ord(char) + shift
            while total_number > ord("Z"):
                total_number -= 26
            encrypted_sentence += chr(total_number)
        elif char.islower() == True and (ord(char) + shift) > ord("z"):
            total_number = ord(char) + shift
            while total_number > ord("z"):
                total_number -= 26
            encrypted_sentence += chr(total_number)
        else:
            encrypted_sentence += chr((ord(char) + shift))
    return encrypted_sentence


def decrypt(sentence, shift):
    """Decrypts the sentence using the shift"""
    decrypted_sentence = ""
    return decrypted_sentence


main()
