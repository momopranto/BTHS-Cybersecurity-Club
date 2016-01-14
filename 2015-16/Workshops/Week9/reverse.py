#output: czkl kdfjkiqkqix
z = raw_input("Gib me input pls")
out = ""
for x,y in enumerate(z):
  if ord(y) >= 97 and ord(y) <= 122:
    out += chr(97 + (((ord(y)-97) + x + len(z) % 26))
  else:
    out += y
print out
