# temperature converter

def temp_conversion(temp, unit):
    """this function convert temperature between Celsius to Fehrenheit"""# dok String

    if unit == 'C':
        return (temp * 9/5) + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
    else:
        return None
print(temp_conversion(25,'C'))
print(temp_conversion(77,"F"))
