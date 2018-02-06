""" Run text through a particular cipher alphabet
    Parameters: text: str Either the plain text to encipher, or the cipher text to decrypt
    cipher_alphabet: dict Dictionary specifying {'original_letter': 'cipher_letter'}
    option: str (default 'encipher')
    'encipher' (accept plain text and output cipher text)
    'decipher' (accept cipher text and output plain text)
    Returns: cipher text by default,     plain text if option is set to decipher
    """
plain_text = list('abcdefghijklmnopqrstuvwxyz')    
cipher = list('hqgiumeaylnofdxjkrcvstzwb')
cipher_code = dict(zip(plain_text, cipher))

def cipher(text, cipher_alphabet=cipher_code, option='encipher'):
    
    encoded_text = ""
    if option == 'encipher':
        for char in text:
            if char.lower() in cipher_alphabet:
                new_char = cipher_alphabet[char.lower()]
                encoded_text += new_char
            elif char == ' ':
                encoded_text += char
    elif option == 'decipher':
        for char in text:
            if char == ' ':
                encoded_text += char
            else:
                for key, value in cipher_alphabet.items():
                    if char.lower() in value:
                        new_char = key
                        encoded_text += new_char
                
    return encoded_text
