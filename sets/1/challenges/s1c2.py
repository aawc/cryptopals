from common import FixedXor

def main():
  a = "1c0111001f010100061a024b53535009181c"
  b = "686974207468652062756c6c277320657965"
  print FixedXor.FixedXor(a, b)

if __name__ == "__main__":
  main()
