logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(text,shift,direction):
    cipher_message = ""
    if direction == 'encode':
        for letter in text:
            if letter.isalpha():
                letter_index = alphabet.index(letter)
                cipher_message += alphabet[(letter_index + shift) % 26]
                # modulo calculates how many letters are "left" beyond 'z' after shifting
                # ensures that encryption wraps around the alphabet
            else:
                cipher_message += letter
        print(f"The encrypted message is: {cipher_message}")
    elif direction == 'decode':
        for letter in text:
            if letter.isalpha():
                letter_index = alphabet.index(letter)
                cipher_message += alphabet[(letter_index - shift) % 26]
            else:
                cipher_message += letter
        print(f"The decrypted message is: {cipher_message}")

print(logo)

again = 'yes'
while again != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text,shift,direction)
    again = input("Do you want to go again? Type yes or no: ").lower()