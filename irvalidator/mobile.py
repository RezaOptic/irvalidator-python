
import re

# country tag -> country code
countries = {'IR': '98'}

def validate(tag, mobile_no):
    """
    validate mobile number
    :param tag: country tag
    :param mobile_no: mobile number
    :type tag: str
    :type mobile_no: str
    :return: True for valid mobile number & False for invalid mobile number
    :rtype: bool
    """""

    # get county code
    countryCode = countries.get(tag.upper())

    # check country tag
    if countryCode == None:
        # country tag not found
        return False

    rgxPattern = ("^(?:0|\+%s|00%s)(\d{10})$" % (countryCode, countryCode))

    pattern = re.compile(rgxPattern)
    if pattern.match(mobile_no):
        return True
    
    return False
    
