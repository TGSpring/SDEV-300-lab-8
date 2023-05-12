"""
Tyler Spring
Lab 8, part2_b
This is the base decrypter. It takes the given string and calls the
function to run it against the base 64 encoder to decrypt and create a new list.
"""
import base64


def d64(in_string):
    dec_str = str(base64.urlsafe_b64decode(in_string.encode("utf_8")))
    return dec_str


def reader2():
    """
Method that contains the encryption, calls the decrypt, then outputs.
    :rtype: object
    """
    in_string = "U28gdGhpcyBpcyBiYXNlNjQuIE5vdyBJIGtub3cu"
    out_string = d64(in_string)
    print("The decrypted base 64 string: {}".format(out_string))


reader2()
