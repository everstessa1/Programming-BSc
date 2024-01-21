# Problem Set 6
# Name: Tessa Evers (#10550062)
# Time: 22:00
# vigenere.py: prints the encrypted plaintext given a keyword


import cs50
import sys
from array import array
inalphabet = 26

def main():

    # Check amount of input arguments
    if len(sys.argv) == 0:
        print("Not enough imput arguments")

    else:
        # If input went right, check if word contains letters and determine length.
        keyword = sys.argv[1]
        n_keyword = len(keyword)
        check_keyword(keyword, n_keyword)

        # If keyword is right, get plaintext and determine length.
        plaintext = get_plaintext()
        n_plaintext = len(plaintext)

        # Encrypt given plaintext and print.
        ciphertext = encrypt_plaintext(keyword, n_keyword, plaintext, n_plaintext)
        print(ciphertext)

    # Function to check the given keyword.
    def check_keyword(keyword, n_keyword):
        for i in range(0, n_keyword):
            if( keyword[i].isalpha == False ):
                print("Error, keyword contains numbers!!")
                break

    # Function to get the plaintext
    def get_plaintext():
        print("Please enter the plaintext!")
        plaintext = cs50.get_string()
        n_plaintext = len(plaintext)
        return plaintext

    # Function to encrypt the given plaintext.
    def encrypt_plaintext(keyword, n_keyword, plaintext, n_plaintext):
        j = 0
        for i in range(0,n_plaintext):

            # Check if element in plaintext is a letter.
            if (plaintext[i].isalpha == True):
                k = j % n_keyword
                key_nr = 'keyword[k]'
                pt_int = 'plaintext[i]'
                ciphertext = plaintext

                # Check if element is uppercase and encrypt.
                if (plaintext[i].isupper == True):
                    if(keyword[k].isupper == True):
                        ciphertext[i] = (pt_int - 'A' + key_nr - 'A') % inalphabet + 'A'
                    else:
                        ciphertext[i] = (pt_int - 'A' + key_nr - 'a') % inalphabet + 'A'

                # If element is lowercase, encrypt as follows.
                else:
                    if(keyword[k].isupper == True):
                        ciphertext[i] = (pt_int - 'a' + key_nr - 'A') % inalphabet + 'a'
                    else:
                        ciphertext[i] = chr((pt_int - 'a' + key_nr - 'a') % inalphabet + 'a')
                j = j + 1

        # Other characters than letters are not necessary to be encrypted.
        return ciphertext

if __name__ == "__main__":
    main()