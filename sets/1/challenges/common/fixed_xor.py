import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from Crypto.Util import strxor

def FixedXor(input_1, input_2):
  decoded_1 = input_1.decode("hex")
  decoded_2 = input_2.decode("hex")
  return strxor.strxor(decoded_1, decoded_2)

def main():
  expected = "746865206b696420646f6e277420706c6179"
  assert expected.decode("hex") == FixedXor(
    "1c0111001f010100061a024b53535009181c",
    "686974207468652062756c6c277320657965"), FixedXor(
    "1c0111001f010100061a024b53535009181c",
    "686974207468652062756c6c277320657965")

if __name__ == "__main__":
  main()
