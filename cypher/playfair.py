import string
def generate_key_table(key):
   key = key.upper().replace("J", "I")
   table = []
   for char in key + string.ascii_uppercase:
       if char not in table and char != "J":
           table.append(char)
   return [table[i:i+5] for i in range(0, 25, 5)]
def prepare_text(text):
   text = text.upper().replace("J", "I").replace(" ", "")
   prepared = ""
   i = 0
   while i < len(text):
       prepared += text[i]
       if i+1 < len(text) and text[i] == text[i+1]:
           prepared += "X"
           i += 1
       elif i+1 < len(text):
           prepared += text[i+1]
           i += 2
       else:
           prepared += "X"
           i += 1
   return prepared
def find_position(table, char):
   for row in range(5):
       for col in range(5):
           if table[row][col] == char:
               return row, col
   return None
def encrypt_pair(table, a, b):
   r1, c1 = find_position(table, a)
   r2, c2 = find_position(table, b)
   if r1 == r2:
       return table[r1][(c1+1)%5] + table[r2][(c2+1)%5]
   elif c1 == c2:
       return table[(r1+1)%5][c1] + table[(r2+1)%5][c2]
   else:
       return table[r1][c2] + table[r2][c1]
def decrypt_pair(table, a, b):
   r1, c1 = find_position(table, a)
   r2, c2 = find_position(table, b)
   if r1 == r2:
       return table[r1][(c1-1)%5] + table[r2][(c2-1)%5]
   elif c1 == c2:
       return table[(r1-1)%5][c1] + table[(r2-1)%5][c2]
   else:
       return table[r1][c2] + table[r2][c1]
def playfair_encrypt(key, plaintext):
   table = generate_key_table(key)
   prepared = prepare_text(plaintext)
   return "".join(encrypt_pair(table, prepared[i], prepared[i+1]) for i in range(0, len(prepared), 2))
def playfair_decrypt(key, ciphertext):
   table = generate_key_table(key)
   return "".join(decrypt_pair(table, ciphertext[i], ciphertext[i+1]) for i in range(0, len(ciphertext), 2))
# Example usage
key = "MONARCHY"
plaintext = "INSTRUMENTS"
ciphertext = playfair_encrypt(key, plaintext)
print("Cipher:", ciphertext)
print("Decrypted:", playfair_decrypt(key, ciphertext))