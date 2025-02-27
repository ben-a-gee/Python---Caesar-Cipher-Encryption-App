message = "Hello, World!"
shift = 7

result = ""

# loop through each of the charactor in the message.
for char in message:
    # it checks if char is in the alphabet (a - z)
    if char.isalpha():
        # Convert charactor to the ASCII code 
        char_code = ord(char)
        
        # Create a new charactor code by adding the shift to the current charactor code
        new_char_code = char_code + shift
        
        # convert the new charactor code to a new charactor
        new_char = chr(new_char_code)
        
        result = result + new_char
    else:
        # otherwise, if the char is not in the alphabet, 
        result = result + char

print(result)
