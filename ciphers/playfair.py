import string
import argparse
import numpy as np

def get_arguments():
    parser = argparse.ArgumentParser(description="Playfair Cipher")
    parser.add_argument("m", type=str, help="Message")
    args = parser.parse_args()
    return args


def get_key_table():
    uniques = []
    alphabet = list(string.ascii_uppercase)
    alphabet.remove("J")
    key = "PLAYFAIREXAMPLE"

    for letter in key:
        if letter not in uniques:
            uniques.append(letter)
    mixed_alphabet = uniques + [item for item in alphabet if item not in uniques]


    return(np.array(mixed_alphabet).reshape(5,5))

def strip_message(message):
    message = message.translate(str.maketrans("", "", string.punctuation))
    message = message.replace(" ", "")
    return message
def get_bigrams(unigrams, encoding):
    unigrams = list(strip_message(unigrams))
    if encoding:
        for i,char in enumerate(unigrams[:-1]):
            if unigrams[i] == unigrams[i+1]:
                unigrams.insert(i+1,"X")
        if len(unigrams) % 2 != 0:
            unigrams.insert(-1, "X")
    unigrams = "".join(unigrams)
    return([unigrams[i:i+2].upper() for i in range(0, len(unigrams), 2)])

def subtitute(key_table, bigrams, status):

    text = ""
    for bigram in bigrams:
        # B1 - Index of first bigram element 
        # B2 - Index of second bigram element
        # R1 - Row Index of B1
        # R2 - Row Index of B2
        # C1 - Column Index of B1
        # C2 - Column Index of B2

        b1 = np.where(key_table==bigram[0])
        r1 = b1[0][0]
        c1 = b1[1][0]

        b2 = np.where(key_table==bigram[1])
        r2 = b2[0][0]
        c2 = b2[1][0]
        
        if r1==r2:
            if status == "encoding":
                c1+=1
                c2+=1
                if c1>4:
                    c1-=5
                if c2>4:
                    c2-=5
            else:
                c1-=1
                c2-=1
                if c1<0:
                    c1+=5
                if c2<0:
                    c2+=5
        elif c1==c2:
            if status == "encoding":
                r1+=1
                r2+=1
                if r1>4:
                    r1-=5
                if r2>4:
                    r2-=5
            else:
                r1-=1
                r2-=1
                if r1<0:
                    r1+=5
                if r2<0:
                    r2+=5
        else:
            if status == "encoding":
                c_temp = c1
                c1 = c2
                c2 = c_temp
            else:
                c_temp = c2
                c2 = c1
                c1 = c_temp
        
        text += key_table[r1, c1] + key_table[r2, c2]
    return text


def encode(message):
    print(f"Message: {message}")
    key_table = get_key_table()
    bigrams = get_bigrams(message, True)
    ciphertext = subtitute(key_table, bigrams, "encoding")
    print(f"Ciphertext: {ciphertext}")
    return ciphertext

def decode(ciphertext):
    key_table = get_key_table()
    bigrams = get_bigrams(ciphertext, False)
    plaintext = subtitute(key_table, bigrams, "decoding")
    print(f"Decoded Plaintext: {plaintext}")

def main():
    args = get_arguments()
    decode(encode(args.m))



if __name__ == "__main__":
    main()
