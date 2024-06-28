'''
Programming Set 4

This assignment will test your proficiency in pattern recognition
and programming in Python.
'''

#Convert a binary string to its base-10 integer representation
def bin_to_dec(binary_string):
    final_ans=0
    new_b=binary_string[::-1]
    for i in range(0,len(binary_string)):
        unit=(2**i)*int(new_b[i])
        final_ans+=unit
    return(final_ans)

#Convert a base-10 number to its binary string representation
def dec_to_bin(number):
    work=number
    bin=""
    while work//2!=0:
        bin+=str(work%2)
        work=work//2
    if work//2==0:
        bin+="1"
    rbin=bin[::-1]
    return(rbin)

#Telephone Cipher
def telephone_cipher(message):
    m=-1
    coded=""
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    for i in range(0,len(message)):
        if encoder_dict[message[i]][0]==encoder_dict[message[i-1]][-1] and i!=0:
            coded+="_"
        letter=encoder_dict[message[i]]
        coded+=letter
    return(coded)

#Telephone Decipher
def telephone_decipher(telephone_string):
    telephone_string+="_"
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    numberlist=[]
    for i in range(0,len(telephone_string)):
        number=""
        if i>0 and telephone_string[i]==telephone_string[i-1]:
            continue
        try:
            if telephone_string[i]==telephone_string[i+1]==telephone_string[i+2]==telephone_string[i+3]:
                number+=telephone_string[i]*4
                numberlist.append(number)
            elif telephone_string[i]==telephone_string[i+1]==telephone_string[i+2]:
                number+=telephone_string[i]*3
                numberlist.append(number)
            elif telephone_string[i]==telephone_string[i+1]:
                number+=telephone_string[i]*2
                numberlist.append(number)
            else:
                number+=telephone_string[i]
                numberlist.append(number)
        except:
            break
        while "_" in numberlist:
            numberlist.remove("_")
        letters=[]
        for i in numberlist:
            letters+=decipher_dict[i]
    return("".join(letters))