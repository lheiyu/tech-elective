"""
Objectives:
-key exchange (diffie-hellman)
-encrypt (shifting) with one time pad (caesar shift)
-decrypt
"""
import random
import math
import sympy 
import cv2 as cv
import os

#CONST
NUM_OF_UNICODE_CHAR = 128

def gcd(a, b):  #greatest common divisor
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g

#dh generated secret common key
def find_public_key(prime_num, primitive_root_num, private_key):
    gen_public_key = (primitive_root_num ** private_key) % prime_num
    return gen_public_key

def find_secret_key(prime_num, private_key, public_key_received):
    gen_secret_key = (public_key_received ** private_key) % prime_num
    return gen_secret_key

#encrypt the one time pad witih DH algorithm
def gen_otp_public(one_time_pad, prime_num, primitive_root_num):
    public_otp = []
    for key in one_time_pad:
        public_key = find_public_key(prime_num, primitive_root_num, key)
        public_otp.append(public_key)
    return public_otp

def gen_common_otp(prime_num, one_time_pad, one_time_pad_public):
    common_otp = []
    for i, key in enumerate(one_time_pad):
        common_private_key = find_secret_key(prime_num, key, one_time_pad_public[i])
        common_otp.append(common_private_key)
    return common_otp

#encrypt plain text with one-time pad by caesar shift
def encrypt(plain_txt, otp):
    encrypted_txt = ""
    for i, letter in enumerate(plain_txt):
        char_code = ord(letter)
        char_code += otp[i]%NUM_OF_UNICODE_CHAR
        if char_code >= NUM_OF_UNICODE_CHAR:
            char_code -= NUM_OF_UNICODE_CHAR
        encrypted_txt = encrypted_txt + chr(char_code)
    return encrypted_txt

#decrypt encrypted text by reversing caesar shift
def decrypt(encrypted_txt, otp):
    decrypted_txt = ""
    for i, letter in enumerate(encrypted_txt):
        char_code = ord(letter)
        if char_code - (otp[i]%NUM_OF_UNICODE_CHAR) < 0:
            char_code = char_code + NUM_OF_UNICODE_CHAR - otp[i]%NUM_OF_UNICODE_CHAR
        else:
            char_code -= otp[i]%NUM_OF_UNICODE_CHAR
        decrypted_txt = decrypted_txt + chr(char_code)
    return decrypted_txt

def img_to_otp(img_dir):
    pass

def img_proc(plain_txt, img_dir):
    #check if all files are jpg in this folder, if not throw an error and terminate the whole thing by indenting all encryption code in if statement
    #list_of_img = [] (one img)
    #find resolution, compare wiht len of plain txt
    #if plain txt longer than resolution, add another, repeat until enough
    #for each img, generate a shuffled array of integers (0, res)
    #use this list of int to gen an array of colour codes, multiply the code with the integer from shuffled array and MOD 1000 
    
    #initialise variables
    otp = []
    img_files = os.listdir(img_dir)
    
    print(img_files)
    

def main():
    plain_txt = "0000"
    #generate random number --> implement img proc !!!!!!!!!!
    otp_a = random.sample(range(1, 300), len(plain_txt))
    otp_b = random.sample(range(1, 300), len(plain_txt))
    
    #both are public
    prime_num = sympy.randprime(len(plain_txt), 500)
    primitive_root_num = primitive_root(prime_num)
    
    #sending from alice to bob (a to b)
    
    public_otp_a = gen_otp_public(otp_a, prime_num, primitive_root_num)
    public_otp_b = gen_otp_public(otp_b, prime_num, primitive_root_num)
    
    common_otp_a = gen_common_otp(prime_num, otp_a, public_otp_b)
    common_otp_b = gen_common_otp(prime_num, otp_b, public_otp_a)
    
    encrypted_txt = encrypt(plain_txt, common_otp_a)
    decrypted_txt = decrypt(encrypted_txt, common_otp_b)
    
    print("plain: " + plain_txt)
    print("encrypted: " + encrypted_txt)
    print("decrypted: " + decrypted_txt)
    
    img_proc(plain_txt, "tech-elective\img_captured")
    
if __name__ == "__main__":
    main()
