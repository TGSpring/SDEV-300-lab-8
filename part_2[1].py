"""
Tyler Spring
Lab 8, part2_a
This is the morse code decrypter. It takes the given string and calls the
function to run it against its dictionary to decrypt and create a new list.
"""
def part_a(encryption):
    part_a_dictionary = {'..-': 'U', '--..--': ', ', '....-': '4', '.....': '5',
                         '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q',
                         '--..': 'Z', '.--': 'W', '-..-.': '/', '..---': '2',
                         '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F',
                         '---': 'O', '-.--': 'Y', '-': 'T', '.': 'E',
                         '.-..': 'L', '...': 'S', '-.--.-': ')',
                         '..--..': '?', '.----': '1', '-----': '0',
                         '-.-': 'K', '-..': 'D', '----.': '9',
                         '-....': '6', '.---': 'J', '.--.': 'P',
                         '.-.-.-': '.', '-.--.': '(', '--': 'M',
                         '-.': 'N', '....': 'H', '---..': '8',
                         '...-': 'V', '--...': '7',
                         '--.': 'G', '...--': '3', '-....-': '-'}
    encryption_list = []

    for morse in encryption.split('/'):
        encrypted = ''
        for char in morse.split():
            encrypted += part_a_dictionary[char]
        encryption_list.append(encrypted)
    return ' '.join(encryption_list)


def reader():
    """
Method that contains the encryption, calls the decrypt, then outputs.
    :rtype: object
    """
    encryption = "- .... .. ... / ... -.. . ...- / ...-- ----- ----- / -.-. .-.. .- ... ... / .... .- ... / ... --- -- . / ... - .-. .- -. --. . / .-. . --.- ..- . ... - ... .-.-.-"
    decripped = part_a(encryption)
    print("Decrypted message {}".format(decripped))


reader()
