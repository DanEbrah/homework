n = 3 #shift by 3
input_str = input("Type Plain Text here: ") # prompts input for user to end plain text


def caesar_encrypt(input_str, n): #encryption class
    input_str = input_str.upper() #caps
    global new_encrypt #global variable so it can be used in the decrypt function
    cipher = ""

    for cur_character in input_str: # i = character of each word
        character = ord(cur_character) # ord returns unicode
        next = character + n # shifting 3 accross

        new = chr(next) # converting  back to string here
        new_encrypt = cipher + new
        cipher = new_encrypt
    
    print(f"Plain Text: {input_str}")
    print(f"Cipher Text: {cipher}")


print("\n")

def caesar_decrypt(input_str, n):
    input_str = input_str.upper()
    decrypted = ""

    for cur_character in new_encrypt: # i = character of each word// getting this form
        character = ord(cur_character) # ord returns unicode
        back = character - n # shifting 3 back


        old_new= chr(back) # converting back to string here
        decrypted = decrypted + old_new
        decrypted1 = decrypted
    
    
    print(f"Decrypted back: {decrypted1}") # printing out the decrypted message back



caesar_encrypt(input_str, n)
print("\n")
caesar_decrypt(input_str, n)