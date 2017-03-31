import string
from common import english_alphabet_freq
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from Crypto.Util import strxor


def score(s):
  total = 0
  freq = english_alphabet_freq.LetterFrequency()
  for c in s:
    c_lower = c.lower()
    if c_lower in freq:
      total += freq[c_lower]
  return total

def sortby(p):
  return score(p[1])

def Decode(s):
  decoded_s = s.decode("hex")
  return max([(
      i, strxor.strxor_c(decoded_s, i)) for i in range(0, 256)], key=sortby)

def main():
  s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  print Decode(s)


if __name__ == "__main__":
  main()
