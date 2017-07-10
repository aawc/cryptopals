import string
from common import english_alphabet_freq
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from Crypto.Util import strxor

def EnglishLikeScore(s):
  total = 0
  freq = english_alphabet_freq.LetterFrequency()
  for c in s:
    c_lower = c.lower()
    if c_lower in freq:
      total += freq[c_lower]
  return total

def SortBy(p):
  return EnglishLikeScore(p[1])

def ScoreAndDecode(s):
  decoded_s = s.decode("hex")
  return max([(
      i, strxor.strxor_c(decoded_s, i)) for i in range(0, 256)], key=SortBy)
