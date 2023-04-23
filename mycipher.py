import sys

def format_output(output):
    row = ""
    lines = ""
    row_count = 0
    for letter in output:
        row += letter 
        if len(row) == 5 and row_count < 9:
            row += " "
            lines += row
            row_count += 1
            row = ""
        elif len(row) == 5 and row_count == 9:
            lines += row +"\n"
            row_count = 0
            row = ""

    return(lines + row + "\n")

def encryption(message, shift):
    message = message.upper()
    characters = ""
    
    for char in message:
      if char.isalpha():
        characters += char
    
    encoded_text = []
    
    for char in characters:
      char_ascii = ord(char)
      new_ascii = char_ascii + shift
      
      if new_ascii > ord("Z"):
        result = (new_ascii - ord("Z")) % 26
        
        if result == 0:
          result = 26
        
        new_ascii = result + 64
    
      encoded_text.append(chr(new_ascii))

    value = ''.join(encoded_text)
    return format_output(value)
   
args = sys.argv

for line in sys.stdin:
    result = encryption(line.strip(), int(args[1]))
    sys.stdout.write(result)