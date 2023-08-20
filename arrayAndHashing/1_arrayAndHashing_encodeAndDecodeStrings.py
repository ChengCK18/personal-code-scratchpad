
def encode(strs):
    encoded=""
    for word in strs:
        encoded += "##"+str(len(word))+word

    return encoded

def decode(full_str):
    result = []
    char_i = 0
    while char_i < len(full_str):
       
        if(full_str[char_i] =="#" and full_str[char_i+1] =="#"):
            word_length = int(full_str[char_i+2])
            result.append(full_str[char_i+3: char_i+3+word_length])
            char_i = char_i+3+word_length

   
    return result




encoded_str = encode(["lint","code","love","you"])
decoded_str = decode(encoded_str)
print(decoded_str)
