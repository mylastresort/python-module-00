import sys


def join_args(args): return ' '.join(word for word in ' '.join(args).split())


def encode(text):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.'}
    return ' '.join(morse.get(letter.upper()) or '/' for letter in text)


if __name__ == '__main__':
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    assert args, 'Expected more than 0 arguments'
    text = join_args(args)
    assert all(word.isalnum() for word in text.split()), 'ERROR'
    print(encode(text))
