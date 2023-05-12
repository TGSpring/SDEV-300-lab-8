"""
Tyler Spring
Lab 8, part2_c
This is the casear decrypter. It takes the given string and calls the
function to run through iterations to decrypt and create a new list.
"""

def cip(string_one, two):
    cip_list = []

    for ciph in string_one.upper().split():
        cip_dec = ""
        for char in ciph:
            if char.isalpha():
                cip_car = chr((ord(char) - two - 65) % 26 + 65)
            else:
                cip_car = char
            cip_dec += cip_car
        cip_list.append(cip_dec)
    return ' '.join(cip_list)


def reader3():
    """
Method that contains the encryption, calls the decrypt, then outputs.
    :rtype: object
    """
    cip_string = "--- Psuwb Ysm ----W oa gc qzsjsf. Bc cbs qcizr dcggwpzm twuifs hvwg cih.--- Sbr Ysm ---"
    cip_d_string = cip(cip_string, 14)
    print("Decrypted message: {}".format(cip_d_string))


reader3()
