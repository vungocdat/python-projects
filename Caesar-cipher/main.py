# Caesar Cipher
# the program will ask for an action: encode (type 'e') or decode (type 'd')
# then ask for a text for the action
# lastly for the shift number

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
'3', '4', '5', '6', '7', '8', '9']
alphabet_lenght = len(alphabet)


def caesar(message_to_process, shift_to_process, action_to_do):
    text = ""
    for i in message_to_process:
        if action == "e":
            #
            if i in alphabet:
                encoded_letter = alphabet.index(i) + shift
                # if it is at the end of the list it will start fro the beginning
                while encoded_letter >= alphabet_lenght:
                    encoded_letter -= alphabet_lenght
                text += alphabet[encoded_letter]
            else:
                text += i
        if action == "d":
            if i in alphabet:
                decoded_letter = alphabet.index(i) - shift
                # if it is at the beginning already it will jump at the end
                while decoded_letter < 0:
                    decoded_letter += alphabet_lenght
                text += alphabet[decoded_letter]
            else:
                text += i
    print(f"Result:\n{text}")

cipher_continue = True

print(logo)
while cipher_continue:
    action = input("\nType 'e' for encode a message or 'd' for decode a message: ").lower()
    message = input("\nType your message:\n").lower()
    shift = int(input("\nSelect a shift number: "))
    caesar(message, shift, action)
    decision = input("Do you want to continue? 'y' for yes or 'n' for no: ").lower()
    if decision == 'n':
        print("Thank you. Good bye!")
        cipher_continue = False
