import string
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Caesar Cipher")
    parser.add_argument("m", type=str, help="Message")
    parser.add_argument("s", type=int, help="Shift. Negative Values for Left-Shift. Positive Values for Right-Shift")
    args = parser.parse_args()
    return args


def get_alphabets(shift):
    alphabet = list(string.ascii_uppercase)
    shift = shift % 26
    if shift>0:
        l_first = alphabet[0:shift]
        l_second = alphabet[shift:]
        shifted_alphabet = l_second+l_first
    else:
        r_first = alphabet[shift:]
        r_second = alphabet[0:shift]
        shifted_alphabet = r_second+r_first
    return zip(alphabet, shifted_alphabet)

def encode(message, shift):
    print(f"Message: {message}")
    encoding_alphabet = dict(get_alphabets(shift))
    encoding_alphabet[" "] = " "

    ciphertext = ""
    for char in message:
        ciphertext+=encoding_alphabet[char.upper()]

    print(f"Ciphertext {ciphertext}")
    return ciphertext

def decode(ciphertext, shift):
    decoding_alphabet = dict(get_alphabets(shift))
    decoding_alphabet[" "] = " "
    decoding_alphabet = {v:k for k,v in decoding_alphabet.items()}


    plaintext = ""
    for char in ciphertext:
        plaintext+=decoding_alphabet[char.upper()]
    print(f"Decoded plaintext: {plaintext}")
    return plaintext

def main():
    args = get_arguments()
    decode(encode(args.m, args.s), args.s)
    

if __name__ == "__main__":
    main()

