import itertools

def MultipleCharacterXOR(input, key):
  out = ""
  for i, j in itertools.izip_longest(range(len(input)), range(len(key))):
    vi = i
    vj = j
    if vi is None:
      vi = vj % len(input)
    elif vj is None:
      vj = vi % len(key)
    input_c = input[vi]
    key_c = key[vj]
    out += chr(ord(input_c) ^ ord(key_c))
  return out.encode("hex")

if __name__ == "__main__":
  input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
  key = "ICE"
  print MultipleCharacterXOR(input, key)

