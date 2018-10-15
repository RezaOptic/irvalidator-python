def validate(national_id):
    """
    validate national id number
    :param national_id: national id number
    :type national_id: str
    :return: True for valid national id & False for invalid national id
    :rtype: bool
    """""
    national_id = "0" * (len(national_id) - 10) + national_id
    national_id = list(map(int, national_id[::-1]))
    temp = 0
    for index, digit in enumerate(national_id[1:]):
        temp += digit * (index+2)
    r = divmod(temp, 11)[1]
    if r < 2 and r == national_id[0]:
        return True
    elif r >= 2 and (11 - r) == national_id[0]:
        return True
    return False
