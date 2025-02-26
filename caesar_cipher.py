message = "Hello, World!" 
shift = 17

# loop through each of the charictor in the message.
for char in message:
    # Convert charictor to the ASCII code 
    char_code = ord(char)
    
    # Create a new charactor code by adding the shift to the current charactor code
    new_char_code = char_code + shift
    
    # convert the new charactor code to a new charactor
    new_char = chr(new_char_code)

    print(char, char_code, new_char_code, new_char)
