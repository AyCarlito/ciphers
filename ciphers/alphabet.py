import numpy as np
import caesar
import argparse
import string
import contextlib

def get_arguments():
    parser = argparse.ArgumentParser(description="The Alphabet-Cipher, Lewis Carroll, 1868")
    parser.add_argument("m", type=str, help="Message")
    parser.add_argument("k", type=str, help="Key")
    args = parser.parse_args()
    return args

def get_stripped_message(x):
    return x.replace(" ", "")

def get_repeated_key(key, message):
    return key*(len(message) // len(key)) + key[:len(message) % len(key)]

def get_table():
    alphabet = string.ascii_lowercase

    letter_to_column_index = {}
    alphabet_for_row = {}

    for i, char in enumerate(alphabet):
        with contextlib.redirect_stdout(None):
            alphabet_for_row[char] = list(caesar.encode(alphabet, i))
        letter_to_column_index[char] = i
    return letter_to_column_index, alphabet_for_row

def table_lookup(repeated_key, text):
    letter_to_column_index, alphabet_for_row = get_table()
    temp_text = ""
    for i, char in enumerate(repeated_key):
        row = alphabet_for_row[char]
        column = letter_to_column_index[text[i]]
        temp_text += row[column]
    return temp_text

def encode(key, message):
    print(f"Message: {message}")
    print(f"Key: {key}")
    message = get_stripped_message(message.lower())
    repeated_key = get_repeated_key(key.lower(), message)
    cipher_text = table_lookup(repeated_key, message).lower()

    print(f"Ciphertext: {cipher_text}")
    return cipher_text
    
def decode(key, ciphertext):
    repeated_key = get_repeated_key(key.lower(), ciphertext)
    plaintext = table_lookup(repeated_key, ciphertext).lower()
    print(f"Decoded plaintext: {plaintext}")
    return plaintext
    
def main():
    args = get_arguments()
    decode(args.k, encode(args.k, args.m))


if __name__ == "__main__":
    main()