from common import score_and_decode as sad

def ReadLines(filename):
  content = []
  with open(filename) as f:
    content = [x.rstrip() for x in f.readlines()]
  return content

def SingleCharacterXOR(filename):
  decoded = [sad.ScoreAndDecode(line)[1] for line in ReadLines(filename)]
  scores = [sad.EnglishLikeScore(l) for l in decoded]
  max_index = scores.index(max(scores))
  return max_index, scores[max_index], decoded[max_index]

if __name__ == "__main__":
  print SingleCharacterXOR("4.txt")
