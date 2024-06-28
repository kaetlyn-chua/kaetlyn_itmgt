'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

#Shift Letter
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_letter(letter, shift):
    if letter==" ":
        return(" ")
    else:
        new_letter= (alphabet.find(letter)+shift)%26
        return(alphabet[new_letter])

#Caesar Cipher
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_cipher(message, shift):
    string_list=""
    for i in message:
        if i==" ":
            string_list+=(" ")
        else:
            index= (alphabet.find(i)+shift)%26
            string_list+=(alphabet[index])
    return(string_list)

#Shift By Letter
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_by_letter(letter, letter_shift):
    if letter==" ":
        return(" ")
    else:
        new_index=(alphabet.find(letter)+alphabet.find(letter_shift))%26
        return(alphabet[int(new_index)])

#Vigenere Cipher
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vigenere_cipher(message, key):
    new_keylist=[]
    string_list=[]
    while len(new_keylist)<len(message):
        for i in range(0,len(message)):
            new_keylist+=(key[i%len(key)])
        break

    for j in range(0,len(message)):
        if message[j]==" ":
            string_list+=" "
        else:
            index=(alphabet.find(message[j])+alphabet.find(new_keylist[j]))%26
            string_list+=alphabet[index]
    return("".join(string_list))

#Scytale Cipher
def scytale_cipher(message, shift):
    while len(message)%shift!=0:
        message+="_"
    message_list=[]
    for i in range(0,len(message)):
        message_list+=message[(i // shift) + (len(message) // shift) * (i % shift)]
    return("".join(message_list))

#Scytale De-cipher
def scytale_decipher(message, shift):
    message_list=[]
    col=int(len(message)/shift)
    for i in range(0,shift):
        for j in range(0, col):
            message_list+=message[i+shift*j]
    return("".join(message_list))