#February 16, 2025
#Caeser Cypher

class main:
    def encrypt(plaintext,rollvalue):
        "value is the rolling value like -1 / -2 /... /-n for encryption"
        list_text=list(plaintext)
        result=""
        for char in list_text:
            if ord(char)==90:
                change = 65+(rollvalue-1)#rolling adjustment
            elif ord(char)==122:
                change = 97+(rollvalue-1)#rolling adjustment
            else:
                change = ord(char)+rollvalue
            result+=chr(change)
        return result
    
    def decrypt(text,roll_value):
        "value is the rolling value like -1 / -2 /... /-n for decryption"
        list_text = list(text)
        result=""
        for char in list_text:
            if ord(char)==65:
                change = 90-(roll_value+1)#rolling adjustment
            elif ord(char)==97:
                change = 122-(roll_value+1)#rolling adjustment
            else:
                change = ord(char)-roll_value
            result+=chr(change)
        return result
