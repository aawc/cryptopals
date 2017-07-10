import itertools

def MultipleCharacterXOR(input, key):
  out = ""
  j = 0
  while j < max(len(input), len(key)):
    i = j % len(input)
    k = j % len(key)
    j += 1
    input_c = input[i]
    key_c = key[k]
    out += chr(ord(input_c) ^ ord(key_c))
  return out.encode("hex")

if __name__ == "__main__":
  input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
  key = "ICE"
  print MultipleCharacterXOR(input, key)

