#Random per element Caesar encryption/decryption

'''
This is a little tool. It takes in a string (and a key) and spits out an encrypted message. If the key is left blank, it generates one
It is meant to be a part of a larger project that allows you to send an encrpyted message and key across a LAN in a custom protocol,
to another target. This custom protocol is meant to be an OSI level 7 protocol - application layer.

TO DO:
Encrpytion/Decryption: Add support for white spaces and capitals. Add options to encrypt the white space to another symbol
Platform: 
Build platform where the User can input what to D/Encrypt and which IP addr on local network to send it to. 
Add option to have a global seed or a local_host seed if resending to an address of which you have their certification
Protocol:
Build protocol language
'''

import random

#This is the alphabet. We will be cycling through this often. You can change the size of the alphabet if needed in order to make the 
#brute-force decryption more difficult.
alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]

#This is the main mechanism of encryption. It takes in the current index of the alphabet, then changes the index by the degree. If this
#would exceed the length of the alphabet, it wraps back around to the start of the alphabet.
#Example rotate(0, 1) ---> b; rotate(0, 2) ---> c; rotate(0, 27) ---> b 
def rotate(index, degree):
    return alpha[(index + degree) % len(alpha)]
    
#This is the bread of the program. This takes in a string and a seed (if no seed is provided, then one is generated for you)
# and spits out an encrpyted message.
class encrypt:
    #Declaring local variables
    def __init__(self, content, seed):
        self.content = content
        self.seed = seed
        #This builds a seed if the seed provided is not long enough for the content (or none is given)
        while len(self.seed) < len(self.content):
            seed.append(random.randint(0, len(alpha)))
    
    #The main function       
    def encrypt(self):
        seed = self.seed 
        encrypted_content = []
        
        for i in range(len(self.content)):
            encrypted_content.append(rotate(alpha.index(self.content[i]), seed[i]))
                    
        return encrypted_content
    
    #Deals with printing, makes it legiable and ready to send
    def __str__(self):
        to_print = encrypt(self.content,self.seed).encrypt()
        #This line is gross, but it converts the encypted list into a single unbroken string
        printable = ''.join((list(map(' '.join, to_print))))
        return printable


#Decrpytion works in the exact same way as encryption, save the degree of rotation - this time it is len(alpha) - self.seed[i] instead of self.seed[i]
class decrypt:

    def __init__(self, content, seed):
        self.content = content
        self.seed = seed
        while len(seed) < len(content):
            seed.append(random.randint(0, len(alpha)))
    
    def decyrpt(self):
        decrypted_content = []
        for i in range(len(self.content)):
            decrypted_content.append(rotate(alpha.index(self.content[i]), len(alpha) - self.seed[i]))
        
        return decrypted_content
        
    def __str__(self):
        to_print = decrypt(self.content,self.seed).decyrpt()
        printable = ''.join((list(map(' '.join, to_print))))
        return printable
    
