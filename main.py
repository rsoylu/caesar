import sys

# Acceptable inputs: the alphabet we are working with for the Caesar cipher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to encrypt the input text with a given shift
def encrypt(text, shift):
    encryptedMessage = ""  # Initialize an empty string to hold the encrypted message

    # Loop through each character in the input text
    for i in text:
        if i == " ":  # If the character is a space, keep it as is
            encryptedMessage += " "
        elif i.isupper():  # If the character is uppercase
            actualPos = alphabet.index(i)  # Find the index of the character in the alphabet
            encPos = (actualPos + shift) % 26  # Calculate the new position using the shift
            encryptedMessage += alphabet[encPos]  # Append the encrypted character to the result
        else:  # If the character is lowercase
            actualPos = alphabet.index(i.upper())  # Convert to uppercase to find the index
            encPos = (actualPos + shift) % 26  # Calculate the new position using the shift
            encryptedMessage += alphabet[encPos].lower()  # Convert back to lowercase and append to result
    return encryptedMessage  # Return the fully encrypted message

# Function to decrypt the input text with a given shift
def decrypt(text, shift):
    decryptedMessage = ""  # Initialize an empty string to hold the decrypted message

    # Loop through each character in the input text
    for i in text:
        if i == " ":  # If the character is a space, keep it as is
            decryptedMessage += " "
        elif i.isupper():  # If the character is uppercase
            actualPos = alphabet.index(i)  # Find the index of the character in the alphabet
            encPos = (actualPos - shift) % 26  # Calculate the new position by reversing the shift
            decryptedMessage += alphabet[encPos]  # Append the decrypted character to the result
        else:  # If the character is lowercase
            actualPos = alphabet.index(i.upper())  # Convert to uppercase to find the index
            encPos = (actualPos - shift) % 26  # Calculate the new position by reversing the shift
            decryptedMessage += alphabet[encPos].lower()  # Convert back to lowercase and append to result
    return decryptedMessage  # Return the fully decrypted message

# Function to attempt decryption by trying all possible shifts (brute force attack)
def bruteforce(text):
    for i in range(26):  # Iterate over all possible shifts (1 to 26)
        possibleDecryption = decrypt(text, i + 1)  # Decrypt the text with the current shift
        print("Possible decryption for key(shift) " + str(i + 1) + ": " + possibleDecryption + "\n")  # Print each result

# Main function to handle user interaction
def main():
    response1 = ""  # Variable to store the user's choice
    correctInputs = False  # Boolean to control the loop for getting a valid choice

    # Loop until the user provides a valid choice
    while correctInputs == False:
        response1 = input("Choose an option: \n1.Encryption \n2.Decryption \n3.Brute Force Attack \n \nEnter your choice (1/2/3):")

        # Check if the input is valid (1, 2, or 3)
        if (response1 == '1') or (response1 == '2') or (response1 == '3'):
            correctInputs = True  # Break out of the loop if valid
        else:
            print("Please enter a valid input. ")  # Ask again if invalid input

    print("\n")  # Blank line for formatting

    if response1 == '1':  # If the user chose encryption
        validInput = False  # Boolean to control the loop for getting valid plaintext input
        while validInput == False:
            text = input("\nEnter plaintext: ")  # Get the plaintext input
            # Check if all characters are valid (alphabet or space)
            validInput = all(char in set(alphabet + alphabet.lower() + " ") for char in text) and (text != "")
            if validInput == False:  # If invalid input, ask again
                print("You have entered an invalid character. You may only enter the letters of the English alphabet and spaces.")

        isNumber = False  # Boolean to control the loop for getting a valid shift value
        while isNumber == False:
            shift = input("Key: ")  # Get the shift value (key)
            isNumber = shift.isdigit()  # Ensure the shift value is a number
            if isNumber == False:  # If not a number, ask again
                print("You have entered an invalid input. You may only enter numbers.")

        encrypted = encrypt(text, int(shift))  # Encrypt the input text with the given shift
        print("Ciphertext: " + encrypted)  # Output the encrypted text

    elif response1 == '2':  # If the user chose decryption
        validInput = False  # Boolean to control the loop for getting valid ciphertext input
        while validInput == False:
            text = input("\nEnter ciphertext: ")  # Get the ciphertext input
            # Check if all characters are valid (alphabet or space)
            validInput = all(char in set(alphabet + alphabet.lower() + " ") for char in text) and (text != "")
            if validInput == False:  # If invalid input, ask again
                print("You have entered an invalid character. You may only enter the letters of the English alphabet and spaces.")

        isNumber = False  # Boolean to control the loop for getting a valid shift value
        while isNumber == False:
            shift = input("Key: ")  # Get the shift value (key)
            isNumber = shift.isdigit()  # Ensure the shift value is a number
            if isNumber == False:  # If not a number, ask again
                print("You have entered an invalid input. You may only enter numbers.")

        decrypted = decrypt(text, int(shift))  # Decrypt the input text with the given shift
        print("Decrypted: " + decrypted)  # Output the decrypted text

    elif response1 == '3':  # If the user chose brute force attack
        validInput = False  # Boolean to control the loop for getting valid ciphertext input
        while validInput == False:
            text = input("\nEnter ciphertext: ")  # Get the ciphertext input
            # Check if all characters are valid (alphabet or space)
            validInput = all(char in set(alphabet + alphabet.lower() + " ") for char in text) and (text != "")
            if validInput == False:  # If invalid input, ask again
                print("You have entered an invalid character. You may only enter the letters of the English alphabet and spaces.")

        bruteforce(text)  # Perform a brute force attack on the ciphertext


main()  # Call the main function to run the program
