IBAN_CODES = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
    "G": "16",
    "H": "17",
    "I": "18",
    "J": "19",
    "K": "20",
    "L": "21",
    "M": "22",
    "N": "23",
    "O": "24",
    "P": "25",
    "Q": "26",
    "R": "27",
    "S": "28",
    "T": "29",
    "U": "30",
    "V": "31",
    "W": "32",
    "X": "33",
    "Y": "34",
    "Z": "35"
}


def validate(iban):
    if isinstance(iban, str):
        x = IBAN_CODES[iban[0]]
        k = IBAN_CODES[iban[1]]
        iban = iban[4:] + x + k + iban[2] + iban[3]
        iban = int(iban)
        return iban % 97 == 1
    return False


print(validate("IR062960000000100324200001"))
print(validate("IR130120020000004901194495"))
