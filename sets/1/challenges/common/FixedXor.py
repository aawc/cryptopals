def FixedXor(input_1, input_2):
  return "%x" % (int(input_1, 16) ^ int(input_2, 16))

def main():
  assert "60426042" == FixedXor("deadbeef", "beefdead"), FixedXor(
    "deadbeef", "beefdead")
  assert "746865206b696420646f6e277420706c6179" == FixedXor(
    "1c0111001f010100061a024b53535009181c",
    "686974207468652062756c6c277320657965")

if __name__ == "__main__":
  main()
