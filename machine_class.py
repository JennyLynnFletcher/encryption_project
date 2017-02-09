import random
import math

def isPrime(n):
    return all(n % i for i in range(2,n)) 

def randprime(x,y):    
    primes = [i for i in range(x,y) if isPrime(i) and i != 1]
    n = random.choice(primes)
    return n

class Machine():
    def __init__(self,name):
        self.name = name
        self.public_key = randprime(100,5000)
        self.private_key = randprime(100,5000)
        self.modulus = randprime(100,500)
        self.encryption_key_1 = 0
        self.encryption_key_2 = 0

    def return_modulus(self):
        return self.modulus

    def return_name(self):
        return self.name

    def return_public_key(self):
        return self.public_key
    
    def return_encryption_key_1(self):
        return self.encryption_key_1

    def calculate_key(self,send_machine):
        self.encryption_key_1 = (send_machine.return_public_key()**self.private_key)%self.modulus
        self.encryption_key_2 = (send_machine.return_public_key()**self.private_key)%send_machine.return_modulus()
    
    def encrypt_text(self,text,encrypt_decrypt):
        ciphertext = [0 for i in range(0,len(text))]
        asciivalues = [ord(text[i]) for i in range(0,len(text))]
        for i in range(0,len(asciivalues)):
            x = i + self.encryption_key_1
            offset = x + (encryption_key_2*i)        
            ciphertext[i] = asciivalues[i] + (offset*encrypt_decrypt)
            while ciphertext[i] > 126:
                ciphertext[i] = ciphertext[i] - 94
            while ciphertext[i] < 32:
                ciphertext[i] = ciphertext[i] + 94
            ciphertext[i] = str(chr(ciphertext[i]))
        return ciphertext
