import argparse

STARTING_LEFT = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
STARTING_RIGHT = "PTLNBQDEOYSFAVZKGJRIHWXUMC"

def get_arguments():
    parser = argparse.ArgumentParser(description="Chaocipher - John F.Byrne - 1918")
    parser.add_argument("m", type=str, help="Message")
    args = parser.parse_args()
    return args

def shift_to_zenith(x, amount):
    return(x[amount:] + x[:amount])
 
def shift_zenith_plus_one(x):
    return(x[0] + x[2:14] + x[1] + x[14:])

def shift_zenith_plus_two(x):
    return(x[:2] + x[3:14] + x[2] + x[14:])

def permute_left_alphabet(alphabet, amount):
    alphabet = shift_to_zenith(alphabet, amount)
    alphabet = shift_zenith_plus_one(alphabet)
    return alphabet

def permute_right_alphabet(alphabet, amount):
    alphabet = shift_to_zenith(alphabet, amount)
    alphabet = alphabet[1:] + alphabet[0]
    alphabet = shift_zenith_plus_two(alphabet)
    return alphabet

def chaocipher_process(text, left_alphabet, right_alphabet, encoding):
    temp_text = ""

    for char in text:
        if encoding:
            position =  right_alphabet.find(char)
            temp_text += left_alphabet[position]
        else:
            position = left_alphabet.find(char)
            temp_text +=right_alphabet[position]
        left_alphabet = permute_left_alphabet(left_alphabet, position)
        right_alphabet = permute_right_alphabet(right_alphabet, position)
    return temp_text

def encode(message):
    print(f"Message: {message}")
    ciphertext = chaocipher_process(message, STARTING_LEFT, STARTING_RIGHT, True)
    print(f"Ciphertext: {ciphertext}")
    return ciphertext

def decode(ciphertext):
    plaintext = chaocipher_process(ciphertext, STARTING_LEFT, STARTING_RIGHT, False)
    print(f"Decoded plaintext: {plaintext}")

def main():
    args = get_arguments()
    decode(encode(args.m))

if __name__ == "__main__":
    main()