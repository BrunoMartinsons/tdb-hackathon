print()
print("================")
print()
print("Welcome...")
print()
print("This is an encryption and decryption software...")
print()
print("We use magic to encrypt our messages...")
print()

userInput = input(str("Please enter a message to encrypt: "))

encryptedMSG = ''

for letter in userInput:
    encryptedMSG += chr(ord(letter) + 5)

print(encryptedMSG)

print()
userInput = input(str("Enter the message you want decrypted: "))

decryptedMSG = ' '

for letter in userInput:
    decryptedMSG += chr(ord(letter) - 5)

print("Your decrypted message is:" + (decryptedMSG))
