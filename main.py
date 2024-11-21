# Importing the logo from art.py
import art

print(art.logo)

# Creating an alphabet array
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Function takes user text, how many letters they want to shift their message by, and whether they want to encrypt or decrypt a message (based on agreed number between sender and receiver)
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Checking if user wants to restart program
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Do you want to try again?(yes/no)\n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for your time. Goodbye!")