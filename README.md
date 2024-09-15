# Caesar Cipher
The Caesar Cipher, used by Julius Caesar around 58 BC, is a substitution cipher that shifts letters in a message to make it unreadable if intercepted.

This is a program in python which can encrypt, decrypt, and perform a Brute Force Attack for a message using the Caesar Cipher.

Error handling is included.

## Encryption

The encryption method works by using the mathematical formula for the Caesar Cipher:
```
a = (b + c) mod 26
```
where a is the encrypted letter’s place value, b is the actual letter’s position value, and c is the number of shifts to be done for each letter.

## Decryption

For decryption, we simply use this formula:
```
a = (b - c) mod 26
```
where the variables are the same as before. 

## Brute Force Attack

The brute force attack is done by testing every possible shift on the given message. It's simply running the decryption algorithm for shifts 1 to 26.

# Example 

Encryption:

![image](https://github.com/user-attachments/assets/f03bb7c7-66c7-4f7c-bdd1-8455eba87289)

Decryption:

![image](https://github.com/user-attachments/assets/8b40106c-4eda-4687-b104-4fd3518e6617)

Brute Force Attack[^1]:

![image](https://github.com/user-attachments/assets/85b797da-ae68-41ca-8cdc-050435047e9b)

[^1]:Note: The full response shows all 26 shifts.

