from common import score_and_decode as sad
from common import read_lines

def SingleCharacterXOR(f):
  decoded = [sad.ScoreAndDecode(line)[1] for line in read_lines.ReadLines(f)]
  scores = [sad.EnglishLikeScore(l) for l in decoded]
  max_index = scores.index(max(scores))
  return max_index, scores[max_index], decoded[max_index]

if __name__ == "__main__":
  print SingleCharacterXOR("4.txt")
