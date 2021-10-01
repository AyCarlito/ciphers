import string
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Trifid Cipher")
    parser.add_argument("m", type=str, help="Message")
    args = parser.parse_args()
    return args


GROUP_SIZE = 5

def get_trigrams_and_alphabet():
    uniques = []
    trigrams = []
    alphabet = list(string.ascii_uppercase)
    key = "FELIXMARIEDELASTELLE"
    for letter in key:
        if letter not in uniques:
            uniques.append(letter)
    mixed_alphabet = uniques + [item for item in alphabet if item not in uniques] + [" "]
    trigrams = [(str(i+1)+str(j+1)+str(k+1)) for i in range(3) for j in range(3) for k in range(3)]
    return zip(mixed_alphabet, trigrams)

def strip_message(message):
    message = message.translate(str.maketrans("", "", string.punctuation))
    message+= (5-(len(message) % 5)) * " "
    return message  
    
def encode(message):
    print(f"Message: {message}")
    stripped_message = strip_message(message)
    enciphering_alphabet = dict(get_trigrams_and_alphabet())
    deciphering_alphabet = {v: k for k, v in enciphering_alphabet.items()}
    
    matrices = []
    for char in stripped_message:
        matrices.append(list(enciphering_alphabet[char.upper()]))

    cipher_text = ""
    for i in range(len(stripped_message)//GROUP_SIZE):
        cipher_trigrams = ""
        group = matrices[i*GROUP_SIZE:i*GROUP_SIZE+GROUP_SIZE]
        for j in range(3):
            cipher_trigrams += "".join([trigram[j] for trigram in group])
        cipher_trigrams = ([cipher_trigrams[k:k+3] for k in range(0, len(cipher_trigrams), 3)])
        for cipher_trigram in cipher_trigrams:
            cipher_text += deciphering_alphabet[cipher_trigram]
    print(f"Ciphertext: {cipher_text}")
    return cipher_text

def decode(ciphertext):
    enciphering_alphabet = dict(get_trigrams_and_alphabet())
    deciphering_alphabet = {v: k for k, v in enciphering_alphabet.items()}

    plaintext = ""
    for i in range(len(ciphertext)//GROUP_SIZE):
        group = ciphertext[i*GROUP_SIZE:i*GROUP_SIZE+GROUP_SIZE]
        cipher_trigrams = "".join([enciphering_alphabet[char.upper()] for char in group])
        for j in range(GROUP_SIZE):
            cipher_trigram = ""
            for k in range(j,len(cipher_trigrams), 5):
                cipher_trigram +=cipher_trigrams[k]
            plaintext += deciphering_alphabet[cipher_trigram] 
    print(f"Decoded Plaintext: {plaintext}")
    

def main():
    args = get_arguments()
    decode(encode(args.m))
    
if __name__ == "__main__":
    main()
