def FixedXor(input_1, input_2):
  return "%x" % (int(input_1, 16) ^ int(input_2, 16))

def main():
  a = "1c0111001f010100061a024b53535009181c"
  b = "686974207468652062756c6c277320657965"
  print FixedXor(a, b)

if __name__ == "__main__":
  main()
